
def commonCharacterCount(s1, s2):
    count = 0
    s1 = list(s1)
    s2 = list(s2)
    for char in s1:
        if char in s2:
            count += 1
            # s1.remove(char)
            s2.remove(char)
    return count


if __name__ == "__main__":
    print(commonCharacterCount('aabcc', 'adcaa'))
