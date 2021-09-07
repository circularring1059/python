def maxPath(m, n):
    # res = []
    count = 0

    def backtask(left=0, right=0):
        # print(left, right)
        nonlocal count
        if left == m and right == n:
            count += 1
        else:
            if left < m:
                backtask(left + 1, right)

            if right < n:
                backtask(left, right + 1)

    backtask()
    return count


print(maxPath(5, 5))


def getAns(x=0, y=0, m=0, n=0, num=0):
    if x == m and y == n:
        return 1
    n1 = 0
    n2 = 0
    if x + 1 <= m:
        n1 = getAns(x + 1, y, m, n, num)

    if y + 1 <= n:
        n2 = getAns(x, y + 1, m, n, num)
    return n1 + n2


print(getAns(m=5, n=5))
