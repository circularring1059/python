def nextPermutation(array):
    j = 0
    for i in range(len(array) - 1, 0, -1):
        if array[i] > array[i - 1]:
            for j in range(len(array) - 1, i - 1, -1):
                print(array[j], array[i - 1])
                if array[j] > array[i - 1]:
                    array[j], array[i - 1] = array[i - 1], array[j]
                    left, right = i, len(array) - 1
                    while left <= right:
                        array[left], array[right] = array[right], array[left]
                        left += 1
                        right -= 1
                    return array
    return array


print(nextPermutation([9, 5, 7, 6, 2]))
