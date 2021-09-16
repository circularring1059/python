class Solution():

    def thridMax(self, nums):
        nums = list(set(nums))
        if len(nums) <= 2:
            return max(nums)
        max_first = max(nums)
        max_second = nums[0]  # 初始化

        for i in nums:
            if i == max_first:
                continue
            max_second = max(i, max_second)

        res = nums[0]
        for i in nums:
            if i == max_first or i == max_second:
                continue
            res = max(i, res)
        return res

    def thridMax2(self, nums):
        nums = list(set(nums))
        if len(nums) <= 2:
            return max(nums)
        for i in range(len(nums)):
            s = i
            for j in range(i,len(nums)):
                if nums[j] > nums[s]:
                    s = j
            nums[i],nums[s] = nums[s],nums[i]
            if i == 2:
                break
        return nums[2]

    def thridMax3(self, nums):
        nums = list(set(nums))
        if len(nums) <= 2:
            return max(nums)
        def backtask(nums):
            if len(nums) <= 1:
                return nums
            mid = nums[0]
            left = [nums[i] for i in range(1,len(nums)) if nums[i] <= mid ]
            right = [nums[i] for i in range(1,len(nums)) if nums[i] > mid]
            return backtask(right)+[mid]+backtask(left)
        return backtask(nums)[2]

    def thridMax4(self, nums):
        nums = list(set(nums))
        if len(nums) <= 2:
            return max(nums)

        for i in range(len(nums)-1):
            for j in range(len(nums)-i-1):
                flag = True
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    flag = False
            if flag or i == 2:
                break
        return nums[len(nums)-3]
        # return nums


thrid_max_ins = Solution()
print(thrid_max_ins.thridMax([2, 5, 6, 7]))
print(thrid_max_ins.thridMax2([2, 5, 6, 7]))
print(thrid_max_ins.thridMax3([2, 5, 6, 7]))
print(thrid_max_ins.thridMax4([2, 5, 6, 7]))

# def bu(array):
#     for i in range(len(array)-1):
#         flag = True
#         for j in range(len(array)-i-1):
#             if array[j] > array[j+1]:
#                 array[j], array[j+1] = array[j+1], array[j]
#                 flag = False
#         if flag or i == 2:
#             break
#     return array
#
# print(bu([1,8,3,5,2,9,2,1]))