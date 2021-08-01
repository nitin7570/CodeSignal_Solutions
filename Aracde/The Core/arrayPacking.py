def arrayPacking(a):
    x = ''
    for i in a[::-1]:
        x += "{0:b}".format(i).zfill(8)
    return int(x,2)


if __name__ == "__main__":
    print(arrayPacking([24, 85, 0]))
