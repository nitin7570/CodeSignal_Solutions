def addTwoDigits(n):
    return sum([int(number) for number in str(n)])


if __name__ == "__main__":
    print(addTwoDigits(11))
