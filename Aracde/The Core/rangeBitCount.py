def rangeBitCount(a, b):
    array = range(a, b+1)
    binary_array = []

    for number in array:
        binary_array.append("{0:b}".format(int(number))) 

    count = 0

    for binary_string in binary_array:
        count += binary_string.count('1')

    return count


if __name__ == "__main__":
    print(rangeBitCount(2, 7))
    