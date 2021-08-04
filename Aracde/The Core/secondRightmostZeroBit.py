def secondRightmostZeroBit(n):
    return 2 ** bin(n)[::-1].find('0', bin(n)[::-1].find('0') + 1)


if __name__ == "__main__":
    print(secondRightmostZeroBit(37))
