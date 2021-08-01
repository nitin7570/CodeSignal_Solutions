def extractEachKth(inputArray, k):
    result_array = []
    for i in range(0, len(inputArray)):
        if ((i+1) % k) != 0:
            result_array.append(inputArray[i])
    return (result_array)


if __name__ == "__main__":
    print(extractEachKth([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))
