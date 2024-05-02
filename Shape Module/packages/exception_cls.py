class IntInputError(Exception):
    def __init__(self, message):
        super().__init__(message)
        #This checks if the inicial input, the one of the sides, is exclusively 0, 3 or 4, as strings 

class PointInputError(Exception):
    def __init__(self, message):
        super().__init__(message)
        #This checks if each Vertex is composed by two numbers

class ShapeConstructionError(Exception):
    def __init__(self, message):
        super().__init__(message)
        #This checks for repetitions in the vertex given by the user