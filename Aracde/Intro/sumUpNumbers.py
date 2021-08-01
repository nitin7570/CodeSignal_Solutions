def sumUpNumbers(inputString):
    _sum = 0
    temp = ''
    
    for index in range(0, len(inputString)):
        
        if index == len(inputString)-1 and inputString[index].isnumeric():
            print(temp)
            temp += inputString[index]
            _sum += int(temp)
            return _sum
            
        elif inputString.isnumeric(): return int(inputString)
        
        elif inputString[index].isnumeric() and inputString[index+1].isnumeric():
            temp += inputString[index]
            
        elif inputString[index].isnumeric() and not inputString[index+1].isnumeric():
            temp += inputString[index] 
            # print(temp)
            _sum += int(temp)
            temp = ''
            
    return _sum


if __name__ == "__main__":
    print(sumUpNumbers('2 apples, 12 oranges'))
