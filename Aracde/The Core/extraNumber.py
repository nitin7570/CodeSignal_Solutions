def extraNumber(a, b, c):
    if a == b:
        return c
    if c == b:
        return a
    if a == c:
        return b


if __name__ == "__main__":
    print(extraNumber(2, 7, 2))
