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


print(maxPath(1, 1))


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

def Solution(m,n):
    count = 0
    def backtask(left=0, right=0):
        nonlocal count
        if left == m and right == n:
            count += 1
        else:
            if left < m:
                backtask(left+1, right)
            if right < n:
                backtask(left, right+1)
    backtask()
    return count

print(Solution(5,5))

#跳台阶也一样
def jumpSteps(m):
    count = 0
    def backtask(n=0):
        nonlocal count
        if n == m:
            count += 1
        #跳一层
        if m - n >= 1:
            backtask(n+1)
        #跳二层
        if m - n >= 2:
            backtask(n+2)
    backtask()
    return count

print(jumpSteps(3))

#括号组合数
def bracketCombination(m):
    count = 0
    def backtask(x=0, y=0):
        nonlocal count
        if x == m and y == m:
            count += 1
        else:
            if x < m:
                backtask(x+1, y)
                #先要放入左括号
            if y < x:
                backtask(x, y+1)
    backtask()
    return count

print("有效括号组合的数量是:", bracketCombination(5))

def breaketCombinations(m):
    ret = []
    def backtask(x=0, y=0, res=""):
        if len(res) == m * 2:
            ret.append(res)
        else:
            if x < m:
                backtask(x+1, y, res+"{")
            if y < x:
                backtask(x, y+1, res+"}")
    backtask()
    return ret

print(breaketCombinations(5))
print(len(breaketCombinations(5)))

