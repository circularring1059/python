def choose_sort(arg):
    for i in range(len(arg)-1):
        middle = i
        for y in range(i+1,len(arg)):
            if arg[middle]  >  arg[y]:
                middle = y
        arg[i],arg[middle] = arg[middle],arg[i]
    return arg


class ChooseSort():
    def choose_sort(self, array):
        if len(array) < 2:
            return array

        for i in range(len(array)-1):
            middle = i
            for y in range(i+1, len(array)):
                if array[middle] > array[y]:
                    middle = y
            array[i], array[middle] = array[middle], array[i]
        return array



choose = ChooseSort()
print(choose.choose_sort([2,4,1,8,3]))

def Solution(nums):
    if len(nums) <= 1:
        return nums
    for i in range(len(nums)):
        middle_index = i
        for j in range(i, len(nums)):
            if nums[j] > nums[middle_index]:
                middle_index = j
        #把大的放前面
        nums[i], nums[middle_index] = nums[middle_index], nums[i]
    return  nums

print(Solution([3,5,1,8,0,19]))
