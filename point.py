import math

class Point:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y

    def calculate_distance(self, other: "Point") -> float:
        return round(math.hypot(self.x - other.x, self.y - other.y), 2)

    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: "Point") -> "Point":
        return Point(self.x - other.x, self.y - other.y)
    
    def __mul__(self, k: int) -> "Point":
        return Point(self.x * k, self.y * k)
    
    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"