def firstDigit(inputString):
    for char in inputString:
        if char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return char


if __name__ == "__main__":
    print(firstDigit('var_1__Int'))
