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

    def findMissingRanges1(self, nums, lower, upper):
        # start, end = lower, lower
        res = []
        if not len(nums):
            res.append(str(lower) + "->" + str(upper))
            return res
        if len(nums) == 1:
            if nums[0] == lower:
                res.append(str(lower + 1) + '->' + str(upper))
            elif nums[0] - 1 == lower:
                res.append(str(lower))
                res.append(str(nums[0] + 1) + "->" + str(upper))
            else:
                res.append(str(lower) + "->" + str(nums[0] - 1))
                res.append(str(nums[0] + 1) + "->" + str(lower))
            return res

        if nums[0] - 1 == lower:
            res.append(str(lower))
        elif nums[0] - 1 > lower:
            res.append(str(lower) + "->" + str(nums[0] - 1))
        else:
            start, end = nums[1]+1, nums[1]+1
            for i in range(1, len(nums)):
                if  i == len(nums)-1:
                    if upper == nums[len(nums)-1]:
                        pass
                    elif upper == nums[len(nums)-1] -1:
                        res.append(str(upper))
                    else:
                        res.append(str(nums[len(nums)-1]+1)+ "->" + str(upper))
                    return res
                if nums[i] == nums[i+1]-1:
                    pass
                elif nums[i] == nums[i+1] -2:
                    res.append(str(start))
                else:
                    res.append(str(start)+"->"+str(nums[i+1]-1))
                    start = nums[i+1]+1
            return res


find_missing_ranges = Solution()
print(find_missing_ranges.findMissingRanges([0, 1, 3, 50, 75], 0, 99))
print(find_missing_ranges.findMissingRanges1([0, 1, 3, 50, 75], 0, 99))
print(find_missing_ranges.findMissingRanges1([1], 0, 99))
