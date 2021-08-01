def arithmeticExpression(a, b, c):
    if (a + b) == c:
        return True
    if (a - b) == c:
        return True
    if (a * b) == c:
        return True
    if (a / b) == c:
        return True  
    return False  


if __name__ == "__main__":
    print(arithmeticExpression(2, 3, 5))
