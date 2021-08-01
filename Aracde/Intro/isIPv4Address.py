def isIPv4Address(inputString):
    count = 0
    loop_count = 0
    if inputString.count('.') == 3:
        for octet in inputString.split('.'):
            if octet and octet.isnumeric():
                if int(octet) in range(0, 256) and str(int(octet)) == octet:
                    print(octet)
                    count += 1
    else: return False
    return count == 4


if __name__ == "__main__":
    print(isIPv4Address('172.16.254.1'))
