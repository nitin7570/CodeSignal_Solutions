def avoidObstacles(a):
    i = 2
    while True:
        if all([n % i != 0 for n in a]):
            return i
        i += 1


if __name__ == "__main__":
    print(avoidObstacles([5, 3, 6, 7, 9]))
