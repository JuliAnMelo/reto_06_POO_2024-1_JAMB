"""
example_1 = shape.Triangle([shape.Point(2, 1), shape.Point(5, 4), shape.Point(6, 1)])
example_2 = shape.Equilateral_Triangle([shape.Point(2, 1), shape.Point(4, 4.4641), shape.Point(6, 1)])
example_3 = shape.Isosceles_Triangle([shape.Point(3, 1), shape.Point(4, 5), shape.Point(5, 1)])
example_4 = shape.Scalene_Triangle([shape.Point(3, 1), shape.Point(2, 2.5), shape.Point(6, 0.5)])
example_5 = shape.Rectangle_Triangle([shape.Point(3, 1), shape.Point(3, 5), shape.Point(5, 1)])
example_6 = shape.Tetragon([shape.Point(6, 4), shape.Point(5, -3), shape.Point(-2, -1), shape.Point(-4, 2)]) 
example_7 = shape.Square([shape.Point(-5, -2), shape.Point(3, -2), shape.Point(3, -10), shape.Point(-5, -10)])
example_8 = shape.Rectangule([shape.Point(-3, 2), shape.Point(7, 2), shape.Point(7, -4), shape.Point(-3, -4)]) 
example_9 = shape.Trapezoid([shape.Point(7, -2), shape.Point(-5, 2), shape.Point(-3, 6), shape.Point(3, 3)])
"""

#example_1
3.162, 4.0, 4.243
False
11.405
6.0
71.565, 45.0, 63.435

#example_2
4.0, 4.0, 4.0
True
12.0
6.928
60.0, 60.0, 60.0

#example_3
2.0, 4.123, 4.123
False
10.246
4.0
75.964, 28.072, 75.964

#example_4
1.803, 3.041, 4.472
False
9.316
1.999
133.152, 17.103, 29.745

#example_5
2.0, 4.0, 4.472
False
10.472
4.0
90.0, 26.565, 63.435

#example_6
7.071, 7.28, 3.606, 10.198
False
28.155
42.5
82.185, 139.635, 67.62, 70.56

#example_7
8.0, 8.0, 8.0, 8.0
True
32.0
64.0
90.0, 90.0, 90.0, 90.0

#example_8
10.0, 6.0, 10.0, 6.0
False
32.0
60.0
90.0, 90.0, 90.0, 90.0

#example_9
12.649, 4.472, 6.708, 6.403
False
30.233
37.0
81.87, 90.0, 155.225, 32.905

"""
The_Quadrilateral = shape.Trapezoid([shape.Point(7, -2), shape.Point(-5, 2), shape.Point(-3, 6), shape.Point(3, 3)])

print(The_Quadrilateral.get_edges())
print(The_Quadrilateral.get_is_regular())
print(The_Quadrilateral.get_perimeter())
print(The_Quadrilateral.get_area())
print(The_Quadrilateral.get_inner_angles())
"""