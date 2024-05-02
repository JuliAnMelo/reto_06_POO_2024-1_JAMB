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