def circleOfNumbers(n, firstNumber):
    return (firstNumber + n / 2)%n


if __name__ == "__main__":
    print(circleOfNumbers(10, 2))
