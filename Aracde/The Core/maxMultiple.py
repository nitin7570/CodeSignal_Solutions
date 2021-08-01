def maxMultiple(divisor, bound):
    temp = 0
    while(temp <= bound):
        temp += divisor
    return (temp-divisor)


if __name__ == "__main__":
    print(maxMultiple(3, 10))
