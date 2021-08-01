def arrayReplace(inputArray, elemToReplace, substitutionElem):
    for index, element in enumerate(inputArray):
        if element == elemToReplace:
            inputArray[index] = substitutionElem
    return inputArray


if __name__ == "__main__":
    print(arrayReplace([1, 2, 1], 1, 3))
