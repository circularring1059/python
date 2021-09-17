class Solution():
     def climbStairs(self,n):
         if n <= 2:
             return [1,2][n-1]
         first = 1
         second = 2
         cnt = 2
         while cnt < n:
             cnt += 1
             cur = first + second
             if cnt == n:
                return cur
             first = second
             senond = cur

climb_stairs_ins = Solution()
print(climb_stairs_ins.climbStairs(4))