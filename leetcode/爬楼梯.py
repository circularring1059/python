class Solution():
    def climbStairs(self, n):
        if n <= 2:
            return [1, 2][n - 1]
        first = 1
        second = 2
        cnt = 2
        while cnt < n:
            cnt += 1
            cur = first + second
            if cnt == n:
                return cur
            first = second
            second = cur

    def climbStairs1(self, n):
        def backstack(n):
            if n == 1:
                return 1
            if n == 2:
                return 2

            return backstack(n - 1) + backstack(n - 2)

        return backstack(n)


    def climbStairs2(self, n):
        count = 0
        def backstack(n):
            nonlocal count
            if  n == 0:
                count += 1
            if n > 0:
                backstack(n+1)
            if  n > 1:
                backstack(n+2)
        backstack(n)
        return count



climb_stairs_ins = Solution()
print(climb_stairs_ins.climbStairs(4))
print(climb_stairs_ins.climbStairs1(7))
print(climb_stairs_ins.climbStairs(7))
