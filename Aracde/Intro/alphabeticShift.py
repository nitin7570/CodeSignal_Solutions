def alphabeticShift(inputString):
    result_string = []
    for char in inputString:
        if char in ['z', 'Z']:
            result_string.append('a')
        else:
            result_string.append(chr(ord(char)+1))
        
    return ''.join(result_string)


if __name__ == "__main__":
    print(alphabeticShift('crazy'))
