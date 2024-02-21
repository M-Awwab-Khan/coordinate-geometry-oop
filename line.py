import math
from point import Point

class Line:

    def __init__(self, y_intercept: int | float, slope: int | float, mode: str = 'slope_intercept') -> None:
        self.y_intercept = y_intercept
        self.slope = slope
        self.mode = mode
        if self.slope != 0:
            self.x_intercept = -(self.y_intercept / self.slope)
        else:
            self.x_intercept = None

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
    def from_point_slope(cls, p: Point, slope: int | float) -> 'Line':
        y_intercept = p.y - (slope * p.x)
        return cls(y_intercept, slope, mode='point_slope')
    
    @classmethod
    def from_interepts(cls, x_intercept: int | float, y_intercept: int | float) -> 'Line':
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
        

