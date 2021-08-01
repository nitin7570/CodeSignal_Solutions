def spiralNumbers(n):
    A = [[0] * n for _ in range(n)]
    i = j = di = 0
    dj = 1
    for A[i][j] in range(1, n**2 + 1):
        if A[(i+di) % n][(j+dj) % n]:
            di, dj = dj, -di
        i += di
        j += dj
    return A


if __name__ == "__main__":
    print(spiralNumbers([[1, 2, 3],[8, 9, 4],[7, 6, 5]]))
