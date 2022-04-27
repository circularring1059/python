def canJump(nums):
    if  len(nums) <= 1:
        return True

    if nums[0] == 0:
        return False

    max_jump = nums[0]

    #从第二点开始到倒数第个二点
    for i in range(1,len(nums)-1):
        #先判断是否可以跳到该点
        if max_jump < i:
            return False
        #在该点能跳的最大长度
        max_jump = max(max_jump, i+nums[i])
        if max_jump >= len(nums)-1:
            return True

    return False


print(canJump([1,0,1]))