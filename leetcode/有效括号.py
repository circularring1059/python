def isValid(string):
    mapping = {")":"(", "]":"[", "}":"{"}
    stack = []
    # for _, char in enumerate(string):
    for char in string:
        if char not in mapping:
            stack.append(char)
        else:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
    return len(stack) == 0
    # return True

print(isValid("([(]))"))


def isValid1(string):
    stack = []
    mapping = {")": "(", "]": "[", "}": "{"}

    for i in range(len(string)):
        if string[i] in ("{", "[", "("):
            stack.append(string[i])
        else:
            # if i == len(string)-1:
            #     if stack:
            #         return False
            # else:
            #     print(stack)
            #     if not stack:
            #         return False
            if not stack:
                return False
            if stack.pop() != mapping[string[i]]:
                return False
    return True

print(isValid1("([)]"))


