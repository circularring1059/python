def quick_sort(array):
    if len(array) < 2:
        return array

    middle = array[0]
    left = [i for i in array[1::] if i <= middle ]
    right = [i for i in array[1::] if i > middle ]
    return quick_sort(left) + [middle] + quick_sort(right)

print(quick_sort([2,5,4,8,1]))


class QuickSort():
    def quick_sort(self, array):
        if len(array) < 2:
            return array
        middle = array[-1]
        #从小到大排 左边小
        left = [i for i in array[:len(array)-1] if i <= middle ]
        right = [i for i in array[:len(array)-1] if i > middle ]
        return quick_sort(left) + [middle] + quick_sort(right)


quick_sort_ins = QuickSort()
print(quick_sort_ins.quick_sort([1,2,5,3,8,2]))
