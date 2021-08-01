def knapsackLight(value1, weight1, value2, weight2, maxW):
    if (weight1+weight2) <= maxW:
        return value1+value2
    elif ((weight1+weight2)>maxW) and ((weight1<maxW) or (weight2<maxW)):
        return max(value1, value2)
    elif (weight1 > maxW) and (weight2 > maxW):
        return 0
    elif (weight1 == maxW) :
        return value1
    elif (weight2 == maxW):
        return value2


if __name__ == "__main__":
    print(knapsackLight(10, 5, 6, 4, 8))
