def knapsackLight(value1, weight1, value2, weight2, maxW):
    if weight1 + weight2 <= maxW:
        return value1 + value2
    if weight1 <= maxW and weight2 <= maxW:
        return max(value1, value2)
    if weight1 <= maxW:
        return value1
    if weight2 <= maxW:
        return value2
    return 0


if __name__ == "__main__":
    print(knapsackLight(10, 5, 6, 4, 8))
