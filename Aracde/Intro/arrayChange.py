def arrayChange(inputArray):
    moves = 0
    diff = 0
    for index in range(0, len(inputArray)-1):
        if inputArray[index] >= inputArray[index+1]:
            diff = inputArray[index] - inputArray[index+1] + 1
            moves += diff
            inputArray[index+1] += diff
    return moves


if __name__ == "__main__":
    print(arrayChange([1, 1, 1]))
