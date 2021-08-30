def quick_sort(array):
    if len(array) < 2:
        return array

    middle = array[0]
    left = [i for i in array[1::] if i <= middle ]
    right = [i for i in array[1::] if i > middle ]
    return quick_sort(left) + [middle] + quick_sort(right)

print(quick_sort([2,5,4,8,1]))


