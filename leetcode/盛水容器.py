class Solution():
    def maxArea(self, array):
        left, right = 0 , len(array)-1
        if len(array) <= 1:
            print("输入不合法")
        else:
            res = 0
            while left < right:
                if array[left] > array[right]:
                    maxArea = (right-left) * array[right]
                    right -= 1
                else:
                    maxArea = (right-left) * array[left]
                    left += 1
                res = max(res, maxArea)
            return res

solution_ins = Solution()
print(solution_ins.maxArea([1,2,3]))