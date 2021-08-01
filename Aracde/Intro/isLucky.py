def isLucky(n):
    number_list = list(map(int, str(n)))
    length = int(len(str(n))//2)
    return sum(number_list[:length]) == sum(number_list[length:])


if __name__ == "__main__":
    print(isLucky(1230))
