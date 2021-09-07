def maxPath(m, n):
    res = []
    def s(left=0 ,right=0):
        print(left, right)
        if left == m and right == n:
            res.append("*")

        if left < m:
            s(left+1, right)

        if right < n:
            s(left, right+1)


    s()
    return len(res)

print(maxPath(5,5))


def getAns(x=0,y=0, m=0, n=0, num=0):
    if (x == m and y == n):
        return 1
    n1 = 0
    n2 = 0
    if (x + 1 <= m):
        n1 = getAns(x + 1, y, m, n, num)

    if (y + 1 <= n):
        n2 = getAns(x, y + 1, m, n, num)
    return n1 + n2

print(getAns(m=5, n=5))

