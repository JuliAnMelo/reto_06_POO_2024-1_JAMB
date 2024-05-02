import packages.point_cls as point
import packages.line_cls as line
import packages.triangle_cls as triangle
import packages.quadrangle_cls as quadrangle 
import packages.exception_cls as exception

def main():    
    while True:
        print("\n""\t""Hi there:""\n")
        SIDES = input("If you wanna know the measurements of a Triangle,""\t""please type 3""\n"
                      "If you wanna know the measurements of a Quadrilateral,""\t""please type 4""\n"
                      "If you wanna exit the program,""\t\t\t\t""please type 0""\n")
        shape_vertex = ()
        shape_name = "Poligon"
        shape_type = None
        try:    
            if SIDES == "0": 
                print("\t""Have a Nice day, see you again!""\n")
                break
            
            elif SIDES == "3":
                print("\n""Please type the x and y values of each vertex of the Triangle, in sequential order.")
                vertex_A = tuple(map(float, input("\n""First Vertex:""\t\t").split()))
                vertex_B = tuple(map(float, input("\n""Second Vertex:""\t\t").split()))
                vertex_C = tuple(map(float, input("\n""Third Vertex:""\t\t").split()))

                if len(vertex_A) != 2 or len(vertex_B) != 2 or len(vertex_C) != 2:
                    raise exception.PointInputError("Invalid Vertex, please type two numbers per vertex.")
                elif len({vertex_A, vertex_B, vertex_C}) != 3:
                    raise exception.ShapeConstructionError("Each Vertex must be different, please type them again.")

                else:
                    edge_AB = round(line.Line(point.Point(vertex_A[0], vertex_A[1]), 
                                              point.Point(vertex_B[0], vertex_B[1])).compute_length(), 3)
                    edge_BC = round(line.Line(point.Point(vertex_B[0], vertex_B[1]), 
                                              point.Point(vertex_C[0], vertex_C[1])).compute_length(), 3)
                    edge_CA = round(line.Line(point.Point(vertex_C[0], vertex_C[1]), 
                                              point.Point(vertex_A[0], vertex_A[1])).compute_length(), 3)
                    
                    edges = sorted([edge_AB, edge_BC, edge_CA])
                    shape_vertex = (point.Point(vertex_A[0], vertex_A[1]), 
                                    point.Point(vertex_B[0], vertex_B[1]), 
                                    point.Point(vertex_C[0], vertex_C[1]))
                    
                    if edges[0] == edges[1] and edges[1] == edges[2]:
                        shape_name = "Equilateral Triangle"
                        shape_type = triangle.Equilateral(shape_vertex)

                    if (edges[0] == edges[1] and edges[1] != edges[2]) or (edges[0] != edges[1] and edges[1] == edges[2]):
                        shape_name = "Isosceles Triangle"
                        shape_type = triangle.Isosceles(shape_vertex)

                    if edges[0] != edges[1] and edges[1] != edges[2]:
                        shape_name = "Scalene Triangle"
                        shape_type = triangle.Scalene(shape_vertex)  

            elif SIDES == "4":
                print("\n""Please type the x and y values of each vertex of the Quadrilateral, in sequential order.")
                vertex_A = tuple(map(float, input("\n""First Vertex:""\t\t").split()))
                vertex_B = tuple(map(float, input("\n""Second Vertex:""\t\t").split()))
                vertex_C = tuple(map(float, input("\n""Third Vertex:""\t\t").split()))
                vertex_D = tuple(map(float, input("\n""Fourth Vertex:""\t\t").split()))

                if len(vertex_A) != 2 or len(vertex_B) != 2 or len(vertex_C) != 2 or len(vertex_D) != 2:
                    raise exception.PointInputError("Invalid Vertex, please type two numbers per vertex.")
                elif len({vertex_A, vertex_B, vertex_C, vertex_D}) != 4:
                    raise exception.ShapeConstructionError("All Vertex must be different, please type them again.")                

                else:
                    edge_AB = round(line.Line(point.Point(vertex_A[0], vertex_A[1]), 
                                              point.Point(vertex_B[0], vertex_B[1])).compute_length(), 3) 
                    edge_BC = round(line.Line(point.Point(vertex_B[0], vertex_B[1]), 
                                              point.Point(vertex_C[0], vertex_C[1])).compute_length(), 3)
                    edge_CD = round(line.Line(point.Point(vertex_C[0], vertex_C[1]), 
                                              point.Point(vertex_D[0], vertex_D[1])).compute_length(), 3)
                    edge_DA = round(line.Line(point.Point(vertex_D[0], vertex_D[1]), 
                                              point.Point(vertex_A[0], vertex_A[1])).compute_length(), 3)
                    
                    edges = sorted([edge_AB, edge_BC, edge_CD, edge_DA])
                    shape_vertex = (point.Point(vertex_A[0], vertex_A[1]), 
                                    point.Point(vertex_B[0], vertex_B[1]), 
                                    point.Point(vertex_C[0], vertex_C[1]), 
                                    point.Point(vertex_D[0], vertex_D[1]))

                    if edges[0] == edges[1] and edges[1] == edges[2] and edges[2] == edges[3]:
                        shape_name = "Square"
                        shape_type = quadrangle.Square(shape_vertex)

                    if edges[0] == edges[1] and edges[1] != edges[2] and edges[2] == edges[3]:
                        shape_name = "Rectangule"
                        shape_type = quadrangle.Rectangule(shape_vertex)

                    if edges[0] != edges[1] or edges[2] != edges[3]:
                        shape_name = "Trapezoid"
                        shape_type = quadrangle.Trapezoid(shape_vertex)       
            else:
                raise exception.IntInputError("Invalid Input, please try again.")
            
            print("\n""\t"f"The Shape is a {shape_name}""\n")
            print(f"The Shape Edges are:           {shape_type.get_edges()}""\n")
            print(f"The Shape is Regular:          {shape_type.get_is_regular()}""\n")
            print(f"The Shape Perimeter is:        {shape_type.get_perimeter()}""\n")
            print(f"The Shape Area is:             {shape_type.get_area()}""\n")
            print(f"The Shape Inner Angles are:    {shape_type.get_inner_angles()}""\n")    

        except exception.IntInputError as error:
            print("\n""\t"f"Error: {error}""\n")
        except ValueError:
            print("\n""\t"f"Error: Invalid Vertex, please type Numbers.""\n")   
        except exception.PointInputError as error:
            print("\n""\t"f"Error: {error}""\n")
        except exception.ShapeConstructionError as error:   
            print("\n""\t"f"Error: {error}""\n")
        
if __name__ == "__main__": 
    main()