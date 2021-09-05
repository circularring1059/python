class Solution():
    def uniquePath(self, m, n):
        k = m + n -2
        t = m-1

        up = 1
        for i in range(0, t):
            up *= k-i

        down = 1
        for i in range(1, m):
            down *= 1
        return up // down

soultion_ins = Solution()

print(soultion_ins.uniquePath(2,2))