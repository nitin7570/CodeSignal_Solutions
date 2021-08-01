def absoluteValuesSumMinimization(a):
    temp_dict = {}
    for element in a:
        _sum = 0
        for index in range(0, len(a)):
            _sum += abs(a[index] - element)
        temp_dict[element] = _sum
        
    for key, value in temp_dict.items():
        if value == min(temp_dict.values()):
            return key        


if __name__ == "__main__":
    print(absoluteValuesSumMinimization([2, 4, 7]))
