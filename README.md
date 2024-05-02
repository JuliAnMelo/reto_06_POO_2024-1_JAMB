# **Challenge 06 Object Oriented Programming by Julian Melo**: Exceptions

# **Challenge 01: Improved**
## **Exercise 01: Basic Calculator**
```python
def calculator():
    while True:
        print("\n""\t""Hi there:""\n")
        USER_INPUT = tuple(input(
            "Please type two numbers and an operator (+, -, *, /), or press ENTER to exit:    ").split())
        try:
            if len(USER_INPUT) == 0: break

            elif len(USER_INPUT) == 3:
                numbers = (float(USER_INPUT[0]), float(USER_INPUT[1]))
                operator = USER_INPUT[2]
                result = 0

                if operator == "+": result = numbers[0] + numbers[1]
                elif operator == "-": result = numbers[0] - numbers[1]
                elif operator == "*": result = numbers[0] * numbers[1]
                elif operator == "/":
                    if numbers[1] == 0: raise ZeroDivisionError("Division by 0 doesn't exist")
                    elif numbers[0] % numbers[1] == 0: result = numbers[0] // numbers[1]
                    else: result = numbers[0] / numbers[1]
                else: raise ValueError("Please type an operation sign.")

            else: raise IndexError("Please type TWO numbers and ONE operator.")
            
            print(f"The result of {USER_INPUT[0]} {operator} {USER_INPUT[1]} is {round(result, 3)}""\n\n")

        except ValueError as error: print("\n""\t"f"Error: {error}""\n")
        except IndexError as error: print("\n""\t"f"Error: {error}""\n")
        except ZeroDivisionError as error: print("\n""\t"f"Error: {error}""\n")

if __name__ == "__main__": 
    calculator()      
```
### **Improvements**
You can now exit the program by pressing ENTER, also the input is now taken as a `tuple`:
```python
USER_INPUT = tuple(input(
            "Please type two numbers and an operator (+, -, *, /), or press ENTER to exit:    ").split())
        try:
            if len(USER_INPUT) == 0: break
```

### **Exceptions**
| Exception | Input   | Output  |
| ------------ | ------------ | ------------ |
| `ValueError` | `4 8 16` | `Error: Please type an operation sign.` |
| `ValueError` | `one two +` | `Error: could not convert string to float: 'one'` |
| `IndexError` | `4 8 9 /` | `Error: Please type TWO numbers and ONE operator.` |
| `IndexError` | `9 6` | `Error: Please type TWO numbers and ONE operator.` |
| `IndexError` | `74` | `Error: Please type TWO numbers and ONE operator.` |
| `ZeroDivisionError` | `7 0 /` | `Error: Division by 0 doesn't exist.` |

## **Exercise 02: Palindrome Words**
```python
def palindrome():
    while True:
        print("\n""\t""Hi there:""\n")
        WORD = tuple(input("Please type a word, or press ENTER to exit:    ").split())       
        try:
            if len(WORD) == 0: break

            elif WORD[0].isnumeric() is True: 
                raise ValueError("Please don't type numbers in the word.")

            elif len(WORD) == 1:
                letters = list(WORD[0])
                answer = True
                while len(letters) > 1 and answer == True:
                    if sorted(letters)[0].isnumeric() is True:
                        raise ValueError("Please don't type numbers in the word.")
                    if letters[0] == letters[-1]:
                        del letters[0]
                        del letters[-1]
                    else:
                        answer = False
            else:
                raise IndexError("Please type only one word.")

            print("\n"f"Is the word \"{WORD[0]}\" a palindrome?    {answer}""\n")
        
        except ValueError as error: print("\n""\t"f"Error: {error}""\n")
        except IndexError as error: print("\n""\t"f"Error: {error}""\n")

if __name__ == "__main__": 
    palindrome()
```
### **Improvements**
You can now exit the program by pressing ENTER, also the input is now taken as a `tuple`:
```python
WORD = tuple(input("Please type a word, or press ENTER to exit:    ").split())       
        try:
            if len(WORD) == 0: break
```

### **Exceptions**
| Exception | Input   | Output  |
| ------------ | ------------ | ------------ |
| `ValueError` | `3x4mpl3` | `Error: Please don't type numbers in the word.` |
| `ValueError` | `aaa3aaa` | `Error: Please don't type numbers in the word.` |
| `IndexError` | `example hi` | `Error: Please type only one word.` |

## **Exercise 03: Prime Numbers**
```python
def prime_hunter():
    while True:
        print("\n""\t""Hi there:""\n")
        try:
            NUMBER_LIST = list(map(int, input(
                "Please type a sequence of integers, or press ENTER to exit:    ").split()))
            
            if len(NUMBER_LIST) == 0: break
            else:
                NUMBER_LIST.sort(reverse=True)
                if NUMBER_LIST[-1] < 0: raise ValueError
                else:
                    composite_numbers = {0, 1}
                    for integer in NUMBER_LIST:
                        if integer > 2: 
                            if integer % 2 == 0: 
                                composite_numbers.add(integer)
                            else:
                                divider = 3
                                while divider < (integer / 2):
                                    if integer % divider == 0: 
                                        composite_numbers.add(integer)
                                        break
                                    else: divider += 2     
                            
            prime_numbers = tuple((set(NUMBER_LIST) - composite_numbers))
            if len(prime_numbers) > 0:
                result = ", ".join(map(str, prime_numbers)) 
                print(f"The prime numbers in the given list are: {result}""\n")
            if len(prime_numbers) == 0:
                print("There aren\'t any prime numbers in the list.""\n")
        
        except ValueError: print("\n""\t"f"Error: Please write positive numbers.""\n")

if __name__ == "__main__": 
    prime_hunter()
```
### **Improvements**
You can now exit the program by pressing ENTER:
```python
try:
	NUMBER_LIST = list(map(int, input(
		"Please type a sequence of integers, or press ENTER to exit:    ").split()))
	if len(NUMBER_LIST) == 0: break
```

### **Exceptions**
| Exception | Input   | Output  |
| ------------ | ------------ | ------------ |
| `ValueError` | `two eight eleven` | `Error: Please write positive numbers.` |
| `ValueError` | `-8 -9 0 4` | `Error: Please write positive numbers.` |

## **Exercise 04: Maximum Sum**
```python
def maximum_sum():
    while True:
        print("\n""\t""Hi there:""\n")
        try:
            NUMBER_LIST = list(map(int, input(
                "Please type a sequence of numbers, or press ENTER to exit:    ").split()))
            
            if len(NUMBER_LIST) == 0: break
            else:
                max_sum = NUMBER_LIST[0] + NUMBER_LIST[1]
                index = 0
                while index < len(NUMBER_LIST) - 1:
                    if NUMBER_LIST[index] + NUMBER_LIST[index + 1] > max_sum:
                        max_sum = NUMBER_LIST[index] + NUMBER_LIST[index + 1]
                        index += 1
                    else: index += 1
                    
                print(f"The maximum sum in the list is {max_sum}""\n")

        except ValueError: print("\n""\t"f"Error: Please type numbers.""\n")
        except IndexError: print("\n""\t"f"Error: Please type two or more numbers.""\n")

if __name__ == "__main__": 
    maximum_sum()
```
### **Improvements**
You can now exit the program by pressing ENTER:
```python
try:
	NUMBER_LIST = list(map(int, input("Please type a sequence of numbers, or press ENTER to exit:    ").split()))
	if len(NUMBER_LIST) == 0: break
```

### **Exceptions**
| Exception | Input   | Output  |
| ------------ | ------------ | ------------ |
| `ValueError` | `two four eight` | `Error: Please write numbers.` |
| `IndexError` | `7` | `Error: Please two or more numbers.` |

## **Exercise 05: Same Letters**
```python
def words_with_the_same_letters():
    while True:
        print("\n""\t""Hi there:""\n")
        WORD_LIST = list(map(str, input(
            "Please type a list of words, or press ENTER to exit:    ").split()))
        try:    
            if len(WORD_LIST) == 0: break

            if len(WORD_LIST) == 1: raise IndexError("Please type at least two words.")

            if len(WORD_LIST) > 1:
                anagram_strings = []
                index_one = 0
                while index_one < (len(WORD_LIST) - 1):
                    index_two = index_one + 1   
                    while index_two < len(WORD_LIST):
                        if sorted(list(WORD_LIST[index_one]))[0].isnumeric() is True or sorted(list(WORD_LIST[index_two]))[0].isnumeric() is True:
                            raise ValueError("Please don't type numbers in the words.")
                        
                        elif sorted(list(WORD_LIST[index_one])) != sorted(list(WORD_LIST[index_two])):
                            index_two += 1

                        else:
                            if WORD_LIST[index_one] not in anagram_strings: 
                                anagram_strings.append(WORD_LIST[index_one])
                            if WORD_LIST[index_two] not in anagram_strings: 
                                anagram_strings.append(WORD_LIST[index_two])
                            index_two += 1
                    index_one += 1
            
                result = ", ".join(anagram_strings)
                if len(anagram_strings) > 0:
                    print(f"The words with the same letters are: {result}""\n")
                if len(anagram_strings) == 0:
                    print("There aren\"t any words with the same letters.""\n")

        except IndexError as error: print("\n""\t"f"Error: {error}""\n")
        except ValueError as error: print("\n""\t"f"Error: {error}""\n")

if __name__ == "__main__":
    words_with_the_same_letters()
```
### **Improvements**
You can now exit the program by pressing ENTER:
```python
WORD_LIST = list(map(str, input(
	"Please type a list of words, or press ENTER to exit:    ").split()))
	try:    
		if len(WORD_LIST) == 0: break
```

### **Exceptions**
| Exception | Input   | Output  |
| ------------ | ------------ | ------------ |
| `ValueError` | `79 87 95` | `Error: Please don't type numbers in the words.` |
| `ValueError` | `exa1 exa exa exa1` | `Error: Please don't type numbers in the words.` |
| `ValueError` | `pan pan exe3` | `Error: Please don't type numbers in the words.` |
| `IndexError` | `word` | `Error: Please type at least two words.` |


# **Shape Class: Expanded and Enhanced Part II**
## **The _exception_ class**
Includes three exclusive exceptions, designed with the Shape Packages in mind:
### **IntInputError**
```python
class IntInputError(Exception):
    def __init__(self, message):
        super().__init__(message)
        #This checks if the inicial input, the one of the sides, is exclusively 0, 3 or 4, as strings 
```

### **PointInputError**
```python
class PointInputError(Exception):
    def __init__(self, message):
        super().__init__(message)
        #This checks if each Vertex is composed by two numbers 
```

### **ShapeConstructionError**
```python
class ShapeConstructionError(Exception):
    def __init__(self, message):
        super().__init__(message)
        #This checks for repetitions in the vertex given by the user
```

## **Presenting: _main.py_**
Improved with the `try`/`except` block and structure changes, is ready for possible new changes in mind if needed, read below for further details:
```python
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
```

### **Improvements**
- Modified certain parts of the code for reading comfort:
```python
SIDES = input("If you wanna know the measurements of a Triangle,""\t""please type 3""\n"
			  "If you wanna know the measurements of a Quadrilateral,""\t""please type 4""\n"
              "If you wanna exit the program,""\t\t\t\t""please type 0""\n")
        #...
edge_AB = round(line.Line(point.Point(vertex_A[0], vertex_A[1]), 
                          point.Point(vertex_B[0], vertex_B[1])).compute_length(), 3)
edge_BC = round(line.Line(point.Point(vertex_B[0], vertex_B[1]), 
                          point.Point(vertex_C[0], vertex_C[1])).compute_length(), 3)
edge_CA = round(line.Line(point.Point(vertex_C[0], vertex_C[1]), 
                          point.Point(vertex_A[0], vertex_A[1])).compute_length(), 3)
```
- Change `list` by `tuple` in inputs:
```python
vertex_A = tuple(map(float, input("\n""First Vertex:""\t\t").split()))
vertex_B = tuple(map(float, input("\n""Second Vertex:""\t\t").split()))
vertex_C = tuple(map(float, input("\n""Third Vertex:""\t\t").split()))
vertex_D = tuple(map(float, input("\n""Fourth Vertex:""\t\t").split()))
```
- New `shape_vertex`, `shape_name` and `shape_type` variables, simplifying the output code:
```python 
shape_vertex = ()
shape_name = "Poligon"
shape_type = None
        #...
shape_vertex = (point.Point(vertex_A[0], vertex_A[1]), 
                point.Point(vertex_B[0], vertex_B[1]), 
                point.Point(vertex_C[0], vertex_C[1]))
        #...
shape_name = "Scalene Triangle"
shape_type = triangle.Scalene(shape_vertex)
        #...
print("\n""\t"f"The Shape is a {shape_name}""\n")
print(f"The Shape Edges are:           {shape_type.get_edges()}""\n")
print(f"The Shape is Regular:          {shape_type.get_is_regular()}""\n")
print(f"The Shape Perimeter is:        {shape_type.get_perimeter()}""\n")
print(f"The Shape Area is:             {shape_type.get_area()}""\n")
print(f"The Shape Inner Angles are:    {shape_type.get_inner_angles()}""\n")  
```

### **Exceptions**
| Exception | Message | Input | Output |
| ------------ | ------------ | ------------ | ------------ |
| `IntInputError` | `...please type (3 4 0)` | `8` | `Error: Invalid Input, please try again..` |
| `IntInputError` | `...please type (3 4 0)` | `three` | `Error: Invalid Input, please try again..` |
| `ValueError` | `Please type the x and y values of each vertex...` | `x y` | `Error: Invalid Vertex, please type Numbers.` |
| `PointInputError` | `Please type the x and y values of each vertex...` | `1` | `Error: Invalid Vertex, please type two numbers per vertex.` |
| `PointInputError` | `Please type the x and y values of each vertex...` | `15 9 23` `19 4 24` `0 0 0` | `Error: Invalid Vertex, please type two numbers per vertex.` |
| `ShapeConstructionError` | `Please type the x and y values of each vertex...` | `12 1` `20 3` `12 1` | `Error: Each Vertex must be different, please type them again.` |
