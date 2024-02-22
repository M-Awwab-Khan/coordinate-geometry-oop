import math
from point import Point
from typing import Union

class Line:

    def __init__(self, y_intercept: Union[int, float], slope: Union[int, float], mode: str = 'slope_intercept') -> None:
        self.y_intercept = y_intercept
        self.slope = slope
        self.mode = mode
        if self.slope != 0:
            self.x_intercept = -(self.y_intercept / self.slope)
        else:
            self.x_intercept = None
            self.mode = 'horizontal'

    @classmethod
    def from_two_points(cls, p1: Point, p2: Point) -> 'Line':
        if p1.x == p2.x:
            slope = math.inf
            y_intercept = None
            mode = 'horizontal'
        else:
            slope = (p1.y - p2.y) / (p1.x - p2.x)
            y_intercept = p1.y - (slope * p1.x)
        if slope == 0:
            mode = 'horizontal'
        return cls(y_intercept, slope, mode=mode)
    
    @classmethod
    def from_point_slope(cls, p: Point, slope: Union[int, float]) -> 'Line':
        y_intercept = p.y - (slope * p.x)
        return cls(y_intercept, slope, mode='slope_intercept')
    
    @classmethod
    def from_intercepts(cls, x_intercept: Union[int, float], y_intercept: Union[int, float]) -> 'Line':
        if x_intercept == 0:
            slope = math.inf
            mode = 'vertical'
        elif y_intercept == 0:
            slope = -(y_intercept / x_intercept)
            mode = 'horizontal'
        else:
            slope = -(y_intercept / x_intercept)
            mode = 'intercepts'
        return cls(y_intercept, slope, mode=mode)
    
    @classmethod
    def from_standard(cls, a: Union[int, float], b: Union[int, float], c: Union[int, float]) -> 'Point':
        if b != 0:
            slope = -a / b
            y_interept = -c / b
            mode = 'standard'
        else:
            y_interept = None
            slope = math.inf
            mode = 'vertical'
        return cls(y_interept, slope, mode=mode)

    def find_slope(self) -> Union[int, float]:
        return self.slope
    
    def is_point_on_line(self, p: Point) -> bool:
        return p.y - (self.slope * p.x) - self.y_intercept == 0
    
    def __str__(self) -> str:
        if self.mode == 'slope_intercept':
            return f"y = {self.slope}x + {self.y_intercept}"
        elif self.mode == 'standard':
            return f"{self.slope}x - y = {-self.y_intercept}"
        elif self.mode == 'intercept':
            return f"x/{self.x_intercept} + y/{self.y_intercept} = 1"
        elif self.mode == 'horizontal':
            return f"y = {self.y_intercept}"
        elif self.mode == 'vertical':
            return f"x = {self.x_intercept}"
        

