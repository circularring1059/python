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


class CanJump():
    def __init__(self, array):
        self.array = array

    def can_jump(self):
        if 0 not in self.array or len(self.array) <= 1:
            return True

        if self.array[0] == 0:
            return False

        #在某点能跳跃最大长度,开始是起始位置
        max_length = self.array[0]
        #肯定可以跳到第二个，所以从第二个点开始循环
        for i in range(1, len(self.array)-1):
            max_length = max(max_length, self.array[i] +i)
            if max_length >= len(self.array)-1:
                return True
            #判断能否到下一跳
            if max_length < i+1:
                return False

can_jump_ins =  CanJump([1,1,0,2,0])
print(can_jump_ins.can_jump())
