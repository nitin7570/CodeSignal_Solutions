def arrayMaxConsecutiveSum(inputArray, k):
    total = sum(inputArray[0:k])
    result = total
    for i in range(1, len(inputArray) - k + 1):
        total -= inputArray[i-1] - inputArray[i + k - 1]
        result = max(result, total)
    return result


if __name__ == "__main__":
    print(arrayMaxConsecutiveSum([2, 3, 5, 1, 6], 2))
