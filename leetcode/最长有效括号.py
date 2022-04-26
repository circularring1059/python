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
                    # if lens > max_len:
                    #     max_len = lens
                    max_len = max(max_len, lens)
                else:
                    lens = i + 1
                    # if lens > max_len:
                    #     max_len = lens
                    max_len = max(max_len, lens)
            else:
                stack.append(i)
        i += 1
    return max_len


print(longestValidParentheses("(((())))(()"))


def Solution(str):
    if len(str) <= 1:
        return 0
    stack = [0]
    max_len = 0
    for i in str:
        if i == "(":
            stack.append(0)
        else:
            if len(stack) > 1:
                val = stack.pop()
                stack[-1] += val +2
                max_len = max(max_len, stack[-1])
            else:
                stack = [0]
    return max_len

print(Solution("()(())(("))
print(Solution("(((())))(()"))
