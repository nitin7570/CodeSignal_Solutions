def checkPalindrome(inputString):
    return inputString.lower() == inputString.lower()[::-1]


if __name__ == "__main__":
    print(checkPalindrome('nitin'))
