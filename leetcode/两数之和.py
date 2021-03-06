list1 = []
def two_sum(nums, target):
    dict1 = {}
    for i in range(len(nums)):
        if target-nums[i] in dict1:
            list1.append([dict1[target-nums[i]], i])
            dict1[nums[i]] = i
        else:
            dict1[nums[i]] = i
    return list1

print(two_sum([2,2,7,7,2],9))

