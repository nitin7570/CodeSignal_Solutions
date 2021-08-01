def differentSquares(matrix):
    row = len(matrix)
    col = len(matrix[0])
    uniqueMatrix = []
    
    for i in range(0,row-1):
        for j in range(0,col-1):
            matrix2 = [[matrix[i][j],matrix[i][j+1]],[matrix[i+1][j],matrix[i+1][j+1]]]
            if matrix2 not in uniqueMatrix:
                uniqueMatrix.append(matrix2)
                print(uniqueMatrix)
    
    return len(uniqueMatrix)


if __name__ == "__main__":
    print(differentSquares([[1, 2, 1],[2, 2, 2],[2, 2, 2],[1, 2, 3],[2, 2, 1]]))
