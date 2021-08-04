def mirrorBits(a):
    return int((("{0:b}".format(int(a)))[::-1]), 2)


if __name__ == "__main__":
    print(mirrorBits(8))