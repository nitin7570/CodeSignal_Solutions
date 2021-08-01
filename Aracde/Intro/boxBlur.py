def boxBlur(image):
    result_array = []
    for i in range(len(image)-2):
        result_array.append([])
        for j in range(len(image[0])-2):
            result_array[i].append(sum(image[i][j:j+3] + image[i+1][j:j+3] + image[i+2][j:j+3])/9//1)
    return result_array


if __name__ == "__main__":
    print(boxBlur([[1, 1, 1], [1, 7, 1], [1, 1, 1]]))
