from itertools import permutations


def stringsRearrangement(inputArray):
    for item in permutations(inputArray, len(inputArray)):
        flag = True
        for i in range(len(item) - 1):
            if not dif_equal_one(item[i], item[i + 1]):
                flag = False
                break
        if flag:
            return True
    return False


def dif_equal_one(a, b):
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
    return cnt == 1


if __name__ == "__main__":
    print(stringsRearrangement(["aba", "bbb", "bab"]))
