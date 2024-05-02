from math import acos
from math import degrees

import packages.point_cls as point
import packages.line_cls as line
import packages.shape_cls as shape
import packages.triangle_cls as triangle 


class Tetragon(shape.Shape):
    def __init__(self, vertex: list[point.Point]):
        super().__init__(vertex)
        self.__triangule_1 = triangle.Triangle([vertex[0], vertex[1], vertex[2]])
        self.__triangule_2 = triangle.Triangle([vertex[2], vertex[3], vertex[0]])
        self.edge_1 = line.Line(vertex[0], vertex[1]).compute_length()
        self.edge_2 = line.Line(vertex[1], vertex[2]).compute_length()
        self.__diagonal_1_2 = line.Line(vertex[2], vertex[0]).compute_length()
        self.edge_3 = line.Line(vertex[2], vertex[3]).compute_length()
        self.edge_4 = line.Line(vertex[3], vertex[0]).compute_length()
        self.__diagonal_3_4 = line.Line(vertex[0], vertex[2]).compute_length()

    def compute_perimeter(self):
        self.perimeter = round((self.__triangule_1.compute_perimeter() - self.__diagonal_1_2) 
                               + (self.__triangule_2.compute_perimeter() - self.__diagonal_3_4), 3)
        return self.perimeter
    
    def compute_area(self):
        self.area = round((self.__triangule_1.compute_area() + self.__triangule_2.compute_area()), 3)
        return self.area 
    
    def compute_inner_angles(self):
        __angle_1v2 = acos(((self.edge_1 ** 2) + (self.edge_2 ** 2) - (self.__diagonal_1_2 ** 2))  
                           /  (2 * (self.edge_1 * self.edge_2)) )
        __angle_2vd1 = acos(((self.edge_2 ** 2) + (self.__diagonal_1_2 ** 2) - (self.edge_1 ** 2))  
                            /  (2 * (self.edge_2 * self.__diagonal_1_2)) )
        __angle_d1v1 = acos(((self.__diagonal_1_2 ** 2) + (self.edge_1 ** 2) - (self.edge_2 ** 2))  
                            /  (2 * (self.__diagonal_1_2 * self.edge_1)) )        
        __angle_3v4 = acos(((self.edge_3 ** 2) + (self.edge_4 ** 2) - (self.__diagonal_3_4 ** 2))  
                           /  (2 * (self.edge_3 * self.edge_4)) )
        __angle_4vd2 = acos(((self.edge_4 ** 2) + (self.__diagonal_3_4 ** 2) - (self.edge_3 ** 2))  
                            /  (2 * (self.edge_4 * self.__diagonal_3_4)) )
        __angle_d2v3 = acos(((self.__diagonal_3_4 ** 2) + (self.edge_3 ** 2) - (self.edge_4 ** 2))  
                            /  (2 * (self.__diagonal_3_4 * self.edge_3)) )
   
        __inner_angle_1 = round( abs(degrees(__angle_1v2)), 3)
        __inner_angle_2 = round( abs(degrees(__angle_2vd1 + __angle_d2v3)), 3)
        __inner_angle_3 = round( abs(degrees(__angle_3v4)), 3)
        __inner_angle_4 = round( abs(degrees(__angle_d1v1 + __angle_4vd2)), 3)
        return [__inner_angle_1, __inner_angle_2, __inner_angle_3, __inner_angle_4]
    
    def compute_is_regular(self):
        regular = False
        if (sum(self.__edges) / len(self.__edges)) == self.__edges[0]: 
            regular = True
        return regular

    def get_edges(self):
        self.__edges = [round(self.edge_1, 3), round(self.edge_2, 3), 
                        round(self.edge_3, 3), round(self.edge_4, 3)]
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


class Square(Tetragon):
    def __init__(self, vertex: list[point.Point]):
        super().__init__(vertex)
        self.edge_1 = line.Line(vertex[0], vertex[1]).compute_length()
        self.edge_2 = self.edge_1
        self.edge_3 = self.edge_1
        self.edge_4 = self.edge_1

    def compute_perimeter(self):
        self.perimeter = round((self.edge_1 + self.edge_2 + self.edge_3 + self.edge_4), 3)
        return self.perimeter

    def compute_area(self):
        self.area = round(self.edge_1 * self.edge_1, 3)
        return self.area
    
    def compute_inner_angles(self):
        __inner_angle_1 = round(360 / 4, 3)
        __inner_angle_2 = __inner_angle_1
        __inner_angle_3 = __inner_angle_1
        __inner_angle_4 = __inner_angle_1
        return (__inner_angle_1, __inner_angle_2, __inner_angle_3, __inner_angle_4)


class Rectangule(Tetragon):
    def __init__(self, vertex: list[point.Point]):
        super().__init__(vertex)
        self.edge_1 = line.Line(vertex[0], vertex[1]).compute_length()
        self.edge_2 = line.Line(vertex[1], vertex[2]).compute_length()
        self.edge_3 = self.edge_1
        self.edge_4 = self.edge_2

    def compute_perimeter(self):
        self.perimeter = round((self.edge_1 + self.edge_2 + self.edge_3 + self.edge_4), 3)
        return self.perimeter

    def compute_area(self):
        self.area = round(self.edge_1 * self.edge_2, 3)
        return self.area
    
    def compute_inner_angles(self):
        __inner_angle_1 = round(360 / 4, 3)
        __inner_angle_2 = __inner_angle_1
        __inner_angle_3 = __inner_angle_1
        __inner_angle_4 = __inner_angle_1
        return [__inner_angle_1, __inner_angle_2, __inner_angle_3, __inner_angle_4]
    
    
class Trapezoid(Tetragon):
    def __init__(self, vertex: list[point.Point]):
        super().__init__(vertex)
        self.__triangule_1 = triangle.Triangle([vertex[0], vertex[1], vertex[2]])
        self.__triangule_2 = triangle.Triangle([vertex[2], vertex[3], vertex[0]])
        self.edge_1 = line.Line(vertex[0], vertex[1]).compute_length()
        self.edge_2 = line.Line(vertex[1], vertex[2]).compute_length()
        self.edge_3 = line.Line(vertex[2], vertex[3]).compute_length()
        self.edge_4 = line.Line(vertex[3], vertex[0]).compute_length()

    def compute_perimeter(self):
        self.perimeter = round((self.edge_1 + self.edge_2 + self.edge_3 + self.edge_4), 3)
        return self.perimeter

    def compute_area(self):
        self.area = round((self.__triangule_1.compute_area() + self.__triangule_2.compute_area()), 3)
        return self.area 