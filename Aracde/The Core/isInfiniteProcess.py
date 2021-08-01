def isInfiniteProcess(a, b):
    if b<a:
        return True
    
    if (b-a)%2 ==0:
        return False
    else:
        return True


if __name__ == "__main__":
    print(isInfiniteProcess(2, 6))
