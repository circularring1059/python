def  combinationSum(nums, target):
    res = []
    nums.sort()

    def backtack(remain, temp, start):
        if not remain:
            res.append(temp[:])
        else:
            for i, n in enumerate(nums[start:]):
                if n > remain:
                    break
                backtack(remain-n, temp+[n], start+i)
    backtack(target, [], 0)
    return res



print(combinationSum([1,3,4,5,3,5,3,3,7],8))