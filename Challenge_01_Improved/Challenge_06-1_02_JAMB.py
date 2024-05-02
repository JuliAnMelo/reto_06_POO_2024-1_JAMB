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