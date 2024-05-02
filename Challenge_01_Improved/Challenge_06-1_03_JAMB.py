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