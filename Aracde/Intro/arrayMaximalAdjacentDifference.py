def arrayMaximalAdjacentDifference(inputArray):
    max_diff = 0
    for index in range(len(inputArray)-1):
        if abs(inputArray[index] - inputArray[index+1]) >= max_diff:
            max_diff = abs(inputArray[index] - inputArray[index+1])
    return max_diff


if __name__ == "__main__":
    print(arrayMaximalAdjacentDifference([2, 4, 1, 0]))
