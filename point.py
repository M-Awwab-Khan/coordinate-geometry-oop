import math

class Point:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y

    def calculate_distance(self, other: "Point") -> float:
        return round(math.hypot(self.x - other.x, self.y - other.y), 2)

    def distance_from_origin(self) -> float:
        return round(math.hypot(self.x, self.y), 2)

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
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: "Point") -> "Point":
        return Point(self.x - other.x, self.y - other.y)
    
    def __mul__(self, k: int) -> "Point":
        return Point(self.x * k, self.y * k)
    
    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"