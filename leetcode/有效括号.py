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

    for i in string:
        if i in ("{", "[", "("):
            stack.append(i)
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
            if stack.pop() != mapping[i]:
                return False
    return len(stack) == 0

print(isValid1("(()){"))


