import packages.point_cls as point 

class Shape:
    def __init__(self, vertex: list[point.Point]):
        self.vertex = vertex        

    def compute_perimeter(self):
        pass

    def compute_area(self):
        pass

    def compute_inner_angles(self):
        pass
    
    def compute_is_regular(self):
        pass

    def get_edges(self):
        pass   
    def get_perimeter(self):
        perimeter = self.compute_perimeter()
        return perimeter
    def get_inner_angles(self):
        pass
    def get_area(self):
        area = self.compute_area()
        return area
    def get_is_regular(self):
        regular = self.compute_is_regular()
        return regular