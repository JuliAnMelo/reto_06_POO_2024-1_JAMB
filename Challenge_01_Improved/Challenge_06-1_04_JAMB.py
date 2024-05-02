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