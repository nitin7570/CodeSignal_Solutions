def deleteDigit(n):
    temp_list = []
    for index in range(0, len(str(n))):
        temp = list(str(n))
        del temp[index]
        temp_list.append(temp)
        
    print(temp_list)
    return int(''.join(max(temp_list)))


if __name__ == "__main__":
    print(deleteDigit(152))
