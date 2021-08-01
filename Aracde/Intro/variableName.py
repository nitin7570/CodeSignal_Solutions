def variableName(name):
    return name.replace("_", "").isalnum() and not name[0].isdigit()


if __name__ == "__main__":
    print(variableName('var_1__Int'))
