def sortByHeight(a):
    people_height = []
    
    for element in a:
        if element != -1:
            people_height.append(element)
    
    people_height = sorted(people_height)
    
    i=0
    for index, element in enumerate(a):
        if element != -1:
            a[index] = people_height[i]
            i += 1
    return a


if __name__ == "__main__":
    print(sortByHeight([-1, 150, 190, 170, -1, -1, 160, 180]))
