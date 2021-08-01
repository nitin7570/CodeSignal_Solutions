def adjacentElementsProduct(inputArray):
    max_product = inputArray[0] * inputArray[1]
    for index in range(0, len(inputArray)-1):
        if (inputArray[index] * inputArray[index+1]) > max_product:
            max_product = inputArray[index] * inputArray[index+1]
            print(max_product)
    return max_product


if __name__ == "__main__":
    print(adjacentElementsProduct([3, 6, -2, -5, 7, 3]))
