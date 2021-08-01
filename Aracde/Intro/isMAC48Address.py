import string

def isMAC48Address(inputString):
    
    if len(inputString.split('-')) != 6: return False
    
    i = 0
    
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    for chars in inputString.split('-'):
        if len(chars) == 2:
            print(chars)
            if (chars[0] in nums or chars[0] in string.ascii_uppercase[:6]) and (chars[1] in nums or chars[1] in string.ascii_uppercase[:6]):
                i += 1
    
    return i == 6


if __name__ == "__main__":
    print(isMAC48Address('00-1B-63-84-45-E6'))
