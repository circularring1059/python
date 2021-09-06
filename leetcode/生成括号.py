def generateParenthesis(n):
    res = []
    def  backtrack(s ='', left = 0, right = 0):
        if len(s) == 2 * n :
            print(s)
            res.append(s)
            return res

        if left < n:
            print("*", s, left)
            backtrack(s + "(", left + 1, right)

        if right < n:
            print("**", s,right)
            backtrack(s + ")", left, right+1)
    backtrack()
    return res

print(generateParenthesis(4))