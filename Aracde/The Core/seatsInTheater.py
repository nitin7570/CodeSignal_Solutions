def seatsInTheater(nCols, nRows, col, row):
    return (nCols - col + 1) * (nRows - row)


if __name__ == "__main__":
    print(seatsInTheater(16, 11, 16, 3))
