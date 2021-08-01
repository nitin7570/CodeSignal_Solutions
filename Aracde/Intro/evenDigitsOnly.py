def evenDigitsOnly(n):
    for element in list(map(int, str(n))):
        if element%2 != 0:
            return False
    return True


if __name__ == "__main__":
    print(evenDigitsOnly(248622))
