class Soultion():
    def plusOne(self, nums):
        nums = nums[::-1]
        nums[0] += 1
        for i in range(len(nums)):
            if nums[i] > 9:
                nums[i] -= 10
                if i != len(nums) - 1:
                    nums[i+1] += 1
                else:
                    nums.append(1)
        return nums[::-1]

    def plusOne1(self, nums):
        if nums[0] == 0:
            return [1]
        if nums[len(nums)-1] + 1 < 10:
            nums[len(nums)-1] += 1
            return nums
        nums[len(nums)-2] += 1
        nums[len(nums)-1] = 0
        for i in range(len(nums)-2, -1, -1):
            if nums[i] == 10:
                if i == 0:
                    nums[0] = 0
                    nums.insert(0,1)
                    return nums
                nums[i-1] += 1
                nums[i] = 0
        return nums


puls_one_ins = Soultion()
print(puls_one_ins.plusOne([9,9,9]))
print(puls_one_ins.plusOne1([2,0,9]))

