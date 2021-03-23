def longestValidParentheses(arg):
    if len(arg) == 0 or len(arg) == 1:
        return 0
    stack = []
    max_len = 0
    i = 0
    while i < len(arg):
        if arg[i] == "(":
            stack.append(i)

        if arg[i] == ")":
            if len(stack) and arg[stack[-1]] == "(":
                stack.pop()
                if len(stack):
                    lens = i - stack[-1]
                    if lens > max_len:
                        max_len = lens
                else:
                    lens = i + 1
                    if lens > max_len:
                        max_len = lens
            else:
                stack.append(i)
        i += 1
    return max_len


print(longestValidParentheses("(((())))(()"))
