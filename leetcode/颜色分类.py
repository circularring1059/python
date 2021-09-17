class Soultion():
    def sortColors(self, nums):
        r,w  = 0, 0
        for num in nums:
            if num == 0:
                r += 1
            elif num == 1:
                w += 1

        for i in range(len(nums)):
            if i < r:
                nums[i] = 0
            elif i < r+w:
                nums[i] = 1
            else:
                nums[i] = 2
        return nums

    def sortColors1(self, nums):
        left, right = 0,  len(nums)-1
        i = 0
        while i <= right:
            x = nums[i]
            if x == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left  += 1
                i += 1
            elif x ==2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
            else:
                i += 1
        return nums

sort_colors_ins = Soultion()
print(sort_colors_ins.sortColors([2,0,2,1,1,0]))
print(sort_colors_ins.sortColors1([2,0,2,1,1,0]))
