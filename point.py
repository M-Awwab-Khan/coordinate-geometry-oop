import math

class Point:
    def __init__(self, x: int = 0, y: int = 0, mode='cartesian') -> None:
        self.x = x
        self.y = y
        self.mode = mode
        self.r = round(math.hypot(self.x, self.y), 2)
        self.θ = round(math.atan(self.y / self.x), 2)

    def __getattr__(self, name: str):
        return self.__dict__[f"_{name}"]

    def __setattr__(self, name, value):
        if name == 'mode':
            if value not in ['cartesian', 'polar']:
                raise ValueError('Invalide mode of representation')
        elif type(value) != int and type(value) != float:
            raise TypeError('Invalid type of argument')
        self.__dict__[f"_{name}"] = value

    def calculate_distance(self, other: "Point") -> float:
        return round(math.hypot(self.x - other.x, self.y - other.y), 2)

    def distance_from_origin(self) -> float:
        return self.r

    def which_quadrant(self) -> int:
        if self.x > 0 and self.y > 0:
            return 1
        elif self.x < 0 and self.y > 0:
            return 2
        elif self.x < 0 and self.y < 0:
            return 3
        elif self.x > 0 and self.y < 0:
            return 4

    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y, mode=self.mode)
    
    def __sub__(self, other: "Point") -> "Point":
        return Point(self.x - other.x, self.y - other.y, mode=self.mode)
    
    def __mul__(self, k: int) -> "Point":
        return Point(self.x * k, self.y * k, mode=self.mode)
    
    def __eq__(self, other: "Point") -> bool:
        return (self.x == other.x) and (self.y == other.y)
    
    def mirror_x(self) -> "Point":
        return Point(self.x, -self.y, mode=self.mode)
    
    def mirror_y(self) -> "Point":
        return Point(-self.x, self.y, mode=self.mode)

    @classmethod
    def from_polar_coords(cls, r, θ) -> "Point":
        return cls(r * math.cos(θ), r * math.sin(θ), mode='polar')
    
    def __str__(self) -> str:
        if self.mode == 'cartesian':
            return f"Point(x = {self.x}, y = {self.y})"
        return f"Point(r = {self.r}, θ = {self.θ})"