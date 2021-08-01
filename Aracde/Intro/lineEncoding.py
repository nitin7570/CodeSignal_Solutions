from itertools import groupby

def lineEncoding(s):
    
    x = ''
    for k,g in groupby(s):
        y = len((list(g)))
        if y==1:
            x += k
        else:
            x += str(y) + k
    return x


if __name__ == "__main__":
    print(lineEncoding('aabbbc'))
