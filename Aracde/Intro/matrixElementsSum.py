def matrixElementsSum(matrix):
    
    indexes = []
    elements = []
    
    for row in matrix:
        for index, element in enumerate(row):
            if index not in indexes:
                if row[index] == 0:
                    indexes.append(index)
                else:
                    elements.append(element)
                
    return sum(elements)


if __name__ == "__main__":
    print(matrixElementsSum([[0, 1, 1, 2], [0, 5, 0, 0], [2, 0, 3, 3]]))
