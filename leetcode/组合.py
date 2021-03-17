def generate(n, k):
    res = []
    def backstack(t, cnt, tmp):
        if cnt == 0:
            res.append(tmp[:])
        for i in range(t+1, n+1):
            backstack(i, cnt-1, tmp+[i])
    backstack(0, k, [])
    return res


print(generate(5,3))