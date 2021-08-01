def addBorder(picture):
    result = []
    length = len(picture[0])
    stars_length = length+2
    result.append(stars_length*"*")
    for element in picture:
        string = "*"+ element +"*"
        result.append(string)
    result.append(stars_length*"*")
    return result    



if __name__ == "__main__":
    print(addBorder(["abc","ded"]))
