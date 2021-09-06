# class Solution():
#     def uniquePath(self, m, n):
#         k = m + n -2
#         t = m-1
#
#         up = 1
#         for i in range(0, t):
#             up *= k-i
#
#         down = 1
#         for i in range(1, m):
#             down *= 1
#         return up // down
#
# soultion_ins = Solution()
#
# print(soultion_ins.uniquePath(4,4))
# print("*")
#
# def maxPath(m, n):
#     res = []
#     def s(left=1 ,right=1):
#         # print(left, right)
#         if left == m and right == n:
#             res.append("*")
#
#         if left < m:
#             s(left+1, right)
#
#         if right < n:
#             s(left, right+1)
#
#
#     s()
#     return len(res)
#
# print(maxPath(4,4))
#
#


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

print(getAns(m=2, n=2))

