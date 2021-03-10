def isValid(string):
    mapping = {")":"(", "]":"[", "}":"{"}
    stack = []
    for i, char in enumerate(string):
        if char not in mapping:
            stack.append(char)
        else:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
    return len(stack) == 0
    # return True

print(isValid("([])"))