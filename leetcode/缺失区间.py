class Solution():
    def findMissingRanges(self, nums, lower, upper):
        start, end = lower, lower
        res = []
        for i in range(len(nums)):
            if nums[i] == end:
                start, end = nums[i] + 1, nums[i] + 1
            elif nums[i] > end:
                end = max(end, nums[i] - 1)
                if end != start:
                    res.append(str(start) + "->" + str(end))
                else:
                    res.append(str(start))

                start, end = nums[i] + 1, nums[i] + 1
        if start < upper:
            res.append(str(start) + "->" + str(upper))
        elif start == upper:
            res.append(str(start))

        return res

    def findMissingRanges1(self, nums, lower,  upper):
        start, end = lower, lower
        res = []
        if not len(nums):
            res.append(str(lower)+"->"+str(upper))

        if nums[0]-1 ==  lower:
            res.append(str(lower))
        elif nums[0]-1 >  lower:
            res.append(str(lower)+"->"+str(nums[0]-1))
        else:
            for i in range(1, len(nums)):
                pass




find_missing_ranges = Solution()
print(find_missing_ranges.findMissingRanges( [0, 1, 3, 50, 75],0,99))
print(find_missing_ranges.findMissingRanges( [],0,99))