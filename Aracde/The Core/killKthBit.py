def killKthBit(n, k):
    return int((((bin(n).replace("0b", ""))[::-1])[0:k-1] + '0' + ((bin(n).replace("0b", ""))[::-1])[k:])[::-1], 2)


if __name__ == "__main__":
    print(killKthBit(37, 3))
