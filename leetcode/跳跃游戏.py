def canJump(nums):
    if 0 not in nums or len(nums) <= 1:
        return True

    if nums[0] == 0:
        return False
    #最长跳跃数
    cur = 0
    for i in range(len(nums)):
        if i > cur:
            return False
        cur = max(cur, i + nums[i])
        if cur >= len(nums)-1:
            break
    return True

print(canJump([0,1,0]))