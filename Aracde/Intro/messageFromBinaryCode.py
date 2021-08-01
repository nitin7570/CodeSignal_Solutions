def messageFromBinaryCode(code):
    ret = ""
    for i in range(0, len(code), 8):
        num = int(code[i:i + 8], 2)
        ret += chr(num)
        print(code[i:i + 8])
    return ret


if __name__ == "__main__":
    print(messageFromBinaryCode('010010000110010101101100011011000110111100100001'))
