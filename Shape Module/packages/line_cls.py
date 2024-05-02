from math import asin
from math import degrees

import packages.point_cls as point 

class Line:
    def __init__(self, start: point.Point=0, end: point.Point=0):
        self.start = start
        self.end = end
        self.x_cathetus = self.end.x - self.start.x
        self.y_cathetus = self.end.y - self.start.y

    def compute_length(self):
        hypotenuse = ((self.x_cathetus ** 2) + (self.y_cathetus ** 2)) ** 0.5
        return hypotenuse

    def compute_slope(self):
        hypotenuse = self.compute_length()
        rad = asin(self.y_cathetus / hypotenuse)
        slope = degrees(rad)
        return abs(slope)

    def compute_horizontal_cross(self):
        if self.start.y > 0 and self.end.y > 0:
            return False
        if self.start.y < 0 and self.end.y < 0:
            return False
        else: return True

    def compute_vertical_cross(self):
        if self.start.x > 0 and self.end.x > 0:
            return False
        if self.start.x < 0 and self.end.x < 0:
            return False
        else: return True 