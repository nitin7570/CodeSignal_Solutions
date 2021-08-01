def sudoku(grid):
    
    for row in grid:
        if sorted(row) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print("1")
            return False
    
    for row in grid:
        if sum(row) != 45:
            print("2")
            return False
        
    for index in range(0, len(grid)-1):
        temp = []
        for row in grid:
            temp.append(row[index])
        if sum(temp) != 45: 
            print("3")
            return False
        
    for i in range(0, len(grid), 3):
        arr = []
        for j in range(0, len(grid[0])-1, 3):
            # print(i, " : ", j)
            arr = [grid[i][j], grid[i][j+1], grid[i][j+2],
                    grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2],
                    grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2]]
            if sum(arr) != 45: 
                # print("4")
                return False        
    return True


if __name__ == "__main__":
    print(sudoku([[1, 3, 2, 5, 4, 6, 9, 8, 7],
        [4, 6, 5, 8, 7, 9, 3, 2, 1],
        [7, 9, 8, 2, 1, 3, 6, 5, 4],
        [9, 2, 1, 4, 3, 5, 8, 7, 6],
        [3, 5, 4, 7, 6, 8, 2, 1, 9],
        [6, 8, 7, 1, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 3, 6, 5, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]]))
