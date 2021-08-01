def palindromeRearranging(inputString):
    flag = 0
    temp_dict = {}
    for char in inputString:
        if char in temp_dict.keys():
            temp_dict[char] += 1
        else:
            temp_dict[char] = 1
            
    print(temp_dict)
            
    for value in temp_dict.values():
        if value % 2 == 1:
            flag += 1
    return flag < 2


if __name__ == "__main__":
    print(palindromeRearranging('aabb'))
