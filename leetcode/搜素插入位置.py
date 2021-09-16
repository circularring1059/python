class Solution():

    def searchInsert1(self, nums, target):
        nums.append(target)
        return sorted(list(set(nums))).index(target)

    def searchInsert2(self, nums, target):
        left,right = 0, len(nums)-1
        while left <= right:
            mid = (right + left) //2
            print(mid)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def searchInsert3(self, nums, target):
        for i, num in enumerate(nums):
            if num >= target:
                return i
        return len(nums)



search_index_ins = Solution()
print(search_index_ins.searchInsert1([1,3,5,8,9], 5))
print(search_index_ins.searchInsert2([1,3,5,8,9], 5))
print(search_index_ins.searchInsert3([1,3,5,8,9], 5))