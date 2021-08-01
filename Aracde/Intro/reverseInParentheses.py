def reverseInParentheses(inputString):
    chars = list(inputString)
    bracket_list = []
    for index, char in enumerate(chars):
        if char == "(":
            bracket_list.append(index)
        elif char == ")":
            second_index = bracket_list.pop()
            chars[second_index:index] = chars[index:second_index:-1]
    return ''.join(char for char in chars if char not in '()')


if __name__ == "__main__":
    print(reverseInParentheses('foo(bar)baz'))
