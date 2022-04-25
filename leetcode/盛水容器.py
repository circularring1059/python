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



#盛水最多

def Solutioin(nums):
    left, right = 0, len(nums)-1
    res = 0
    while left < right:
        if nums[left] > nums[right]:
            res = max(res, nums[right] * (right-left))
            right -= 1
        else:
            res = max(res, nums[left] * (right-left))
            left += 1
    return res

print(Solutioin([1,2,3]))

