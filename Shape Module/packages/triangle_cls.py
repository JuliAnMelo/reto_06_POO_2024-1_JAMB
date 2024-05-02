from math import acos
from math import degrees
from math import sqrt

import packages.point_cls as point
import packages.line_cls as line
import packages.shape_cls as shape


class Triangle(shape.Shape):
    def __init__(self, vertex: list[point.Point]):
        super().__init__(vertex)
        __segments = []
        __segment_1 = line.Line(vertex[0], vertex[1]).compute_length()
        __segment_2 = line.Line(vertex[1], vertex[2]).compute_length()
        __segment_3 = line.Line(vertex[2], vertex[0]).compute_length()
        __segments.append(__segment_1)
        __segments.append(__segment_2)
        __segments.append(__segment_3)
        __segments.sort()
        self.edge_1 = __segments[0]
        self.edge_2 = __segments[1]
        self.edge_3 = __segments[2]
        
    def compute_perimeter(self):
        self.perimeter = round((self.edge_1 + self.edge_2 + self.edge_3), 3)
        return self.perimeter
    
    def compute_area(self):
        __semi_perimeter = (self.edge_1 + self.edge_2 + self.edge_3) / 2
        self.area = round(sqrt( __semi_perimeter * (__semi_perimeter - self.edge_1) 
                               * (__semi_perimeter - self.edge_2) * (__semi_perimeter - self.edge_3) ), 3)
        return self.area 

    def compute_inner_angles(self):
        __angle_1v2 = acos(((self.edge_1 ** 2) + (self.edge_2 ** 2) - (self.edge_3 ** 2))  
                           /  (2 * (self.edge_1 * self.edge_2)))
        __angle_2v3 = acos(((self.edge_2 ** 2) + (self.edge_3 ** 2) - (self.edge_1 ** 2))  
                           /  (2 * (self.edge_2 * self.edge_3)))
        __angle_3v1 = acos(((self.edge_3 ** 2) + (self.edge_1 ** 2) - (self.edge_2 ** 2))  
                           /  (2 * (self.edge_3 * self.edge_1)))
        
        __inner_angle_1 = round(abs(degrees(__angle_1v2)), 3)
        __inner_angle_2 = round(abs(degrees(__angle_2v3)), 3)
        __inner_angle_3 = round(abs(degrees(__angle_3v1)), 3)
        return (__inner_angle_1, __inner_angle_2, __inner_angle_3)
    
    def compute_is_regular(self):
        regular = False
        if (sum(self.__edges) / len(self.__edges)) == self.__edges[0]: 
            regular = True
        return regular

    def get_edges(self):
        self.__edges = [round(self.edge_1, 3), round(self.edge_2, 3), round(self.edge_3, 3)]
        return ", ".join(map(str, self.__edges))   
    def get_perimeter(self):
        perimeter = self.compute_perimeter()
        return perimeter
    def get_inner_angles(self):
        inner_angles = ", ".join(map(str, self.compute_inner_angles())) 
        return inner_angles
    def get_area(self):
        area = self.compute_area()
        return area
    def get_is_regular(self):
        regular = self.compute_is_regular()
        return regular

class Equilateral(Triangle):
    def __init__(self, vertex: list[point.Point]):
        super().__init__(vertex)
    def compute_area(self):
        self.area = round((sqrt(3) / 4) * (self.edge_1 ** 2), 3)        
        return self.area 
    
class Isosceles(Triangle):
    def __init__(self, vertex: list[point.Point]):
        super().__init__(vertex)
    def compute_area(self):
        if self.edge_2 == self.edge_3:
            self.__height = sqrt((self.edge_3 ** 2) - ((self.edge_1 / 2) ** 2))
            self.area = round(((self.edge_1 * self.__height) / 2), 3)
            return self.area 
        if self.edge_1 == self.edge_2:
            self.__height = sqrt((self.edge_1 ** 2) - ((self.edge_3 / 2) ** 2))
            self.area = round(((self.edge_3 * self.__height) / 2), 3)
            return self.area 
    
class Scalene(Triangle):
    def __init__(self, vertex: list[point.Point]):
        super().__init__(vertex)
    def compute_area(self):
        __semi_perimeter = self.perimeter / 2
        self.area = round(sqrt(__semi_perimeter * (__semi_perimeter - self.edge_1) 
                               * (__semi_perimeter - self.edge_2) * (__semi_perimeter - self.edge_3) ), 3)
        return self.area 

class TriRectangle(Triangle):
    def __init__(self, vertex: list[point.Point]):
        super().__init__(vertex)
    def compute_area(self):
        self.area = round(((self.edge_1 * self.edge_2) / 2), 3)
        return self.area