def makeArrayConsecutive2(statues):
    
    num_array = [number for number in range(min(statues), max(statues))]
    
    for num in range(min(statues), max(statues)):
        if num in statues:
            num_array.remove(num)
    return len(num_array)


if __name__ == "__main__":
    print(makeArrayConsecutive2([6, 2, 3, 8]))
