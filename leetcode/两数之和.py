def two_sum(nums, target):
    list1,dict1 = [],{}
    for i in range(len(nums)):
        if target-nums[i] in dict1:
            list1.append([dict1[target-nums[i]], i])
            dict1[nums[i]] = i
        else:
            dict1[nums[i]] = i
    return list1

print(two_sum([2,2,7,7,2],9))


def two_sum1(arg, target):
    res = []
    for i in range(len(arg)):
        for j in range(i, len(arg)):
            if arg[i] + arg[j] == target:
                res.append([i, j])
    return(res)

print(two_sum1([2,7,7,2],9))