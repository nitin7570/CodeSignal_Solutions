def allLongestStrings(inputArray):
    result_list = []
    max_length = 0
    
    for string in inputArray:
        if len(string) > max_length:
            max_length = len(string)
            
    for string in inputArray:
        if len(string) == max_length:
            result_list.append(string)
            
    return result_list


if __name__ == "__main__":
    print(allLongestStrings(["aba", "aa", "ad", "vcd", "aba"]))
