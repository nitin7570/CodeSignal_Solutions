def areSimilar(a, b):
    return sorted(a)==sorted(b) and sum([elem_a!=elem_b for elem_a, elem_b in zip(a,b)])<=2


if __name__ == "__main__":
    print(areSimilar([1, 2, 3], [1, 2, 3]))
