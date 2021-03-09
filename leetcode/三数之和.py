def threeSum(nums):
    nums.sort()
    left, res = len(nums), []
    for i in range(len(nums)-2):
        if i  > 0 and nums[i] == nums[i+1]:
            continue
        target = -1 * nums[i]
        j,k = i+1, left-1
        while j < k:
            if nums[j] + nums[k] == target:
                res.append([nums[i], nums[j], nums[k]])
                j= j+1
                while j < k and nums[j] == nums[j-1]:
                     j = j+1
            elif nums[j] + nums[k] < target:
                j = j+1
            else:
                k = k-1
    return res

print(threeSum([0,-2,2,-3,7,3,5]))

#[0,0,0] 没出来
print(threeSum([0,0,0,1,-1]))