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


class TwoSum():
    def two_sum(self, array, target):
        res, dict_tmp = [], {}
        for i in range(len(array)):
            if target -array[i] in dict_tmp:
                res.append([dict_tmp[target-array[i]], i])
                dict_tmp[array[i]] = i
            else:
                dict_tmp[array[i]] = i
        return res


two_sum_ins = TwoSum()
print(two_sum_ins.two_sum([1,2,4,5,2], 9))