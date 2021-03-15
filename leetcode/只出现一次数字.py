def  singleNumber(nums):
    res = 0
    for i  in nums:
        res^=i

    return res


print(singleNumber([1,2,2,3,3]))