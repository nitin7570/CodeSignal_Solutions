def alternatingSums(a):
    a1 = []
    a2 = []
    for index, weight in enumerate(a):
        if index % 2 == 0:
            a1.append(weight)
        else:
            a2.append(weight)
    return [sum(a1), sum(a2)]


if __name__ == "__main__":
    print(alternatingSums([50, 60, 60, 45, 70]))
