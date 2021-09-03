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

            if left + 1 == right:
                return array[right] == target
        return False

binary_find_ins = Binaryfind()
print(binary_find_ins.binary_find([1, 2, 3, 6, 9], 3))

