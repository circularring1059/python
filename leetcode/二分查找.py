class Binaryfind():
    def binary_find(self, array, target):
        left, right = 0, len(array)-1
        while left < right:
            middle_index = int((right+left)/2)

            if array[middle_index] == target:
                return True
            elif array[middle_index] > target:
                right = middle_index
            else:
                left = middle_index

            #这里要后做判断
            if left + 1 == right:
                return array[right] == target

        return False

    def binary_find1(self, array, target):
        if len(array) <= 1:
            return array
        left, right = 0, len(array)-1
        while left <= right:
            mid = (right+left) // 2
            if array[mid] == target:
                return True
            elif array[mid] > target:
                right = mid -1
            else:
                left = mid + 1
        return False

binary_find_ins = Binaryfind()
print(binary_find_ins.binary_find([1, 2, 3], 2))
print(binary_find_ins.binary_find1([1, 2, 3], 2))

