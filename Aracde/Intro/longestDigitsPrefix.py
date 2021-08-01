def longestDigitsPrefix(inputString):
    result = []
    for char in inputString:
        if not char.isnumeric():
            break
        else:
            result.append(char)
    return ''.join(result)


if __name__ == "__main__":
    print(longestDigitsPrefix('123aa1'))
