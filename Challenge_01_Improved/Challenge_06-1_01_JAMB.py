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
                    if numbers[1] == 0: raise ZeroDivisionError("Division by 0 doesn't exist.")
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