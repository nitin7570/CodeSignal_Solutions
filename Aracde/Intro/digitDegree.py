def digitDegree(n):
    
    if len(str(n)) == 1 : return 0

    i = 0
    while(len(str(n)) > 1):
        n = sum(list(map(int, str(n))))
        i += 1
    return i


if __name__ == "__main__":
    print(digitDegree(5))
