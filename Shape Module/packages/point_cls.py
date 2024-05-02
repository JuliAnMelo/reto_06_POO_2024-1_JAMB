class Point:
    def __init__(self, x: float=0, y: float=0):
        self.x = x
        self.y = y
    def move(self, new_x: float, new_y: float):
        self.x = new_x
        self.y = new_y
    def reset(self):
        self.x = 0
        self.y = 0
    def compute_distance(self, point)-> float:
        distance = ((self.x - point.x)**2+(self.y - point.y)**2)**(0.5)
        return distance