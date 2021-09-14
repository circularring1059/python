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
        return nums[2]

    # def thridMax3(self, nums):
    #     nums = list(set(nums))
    #     if len(nums) <= 2:
    #         return max(nums)
    #     def backtask(nums):
    #         if len(nums) <= 1:
    #             return nums
    #         mid = nums[0]
    #         left = [i for i in range(1,len(nums)) if nums[i] <= mid ]
    #         right = [i for i in range(1,len(nums)) if nums[i] > mid]
    #         return backtask(right)+[mid]+backtask(left)
    #     s=backtask(nums)
    #     return s

thrid_max_ins = Solution()
print(thrid_max_ins.thridMax([2, 5, 6, 7]))
print(thrid_max_ins.thridMax2([2, 5, 6, 7]))
print(thrid_max_ins.thridMax3([2, 5, 6, 7]))
