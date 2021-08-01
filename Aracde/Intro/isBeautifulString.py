import string

def isBeautifulString(inputString):

    r = [inputString.count(i) for i in string.ascii_lowercase]
    
    return r[::-1] == sorted(r)


if __name__ == "__main__":
    print(isBeautifulString('bbbaacdafe'))
