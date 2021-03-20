def quick_sort(array):
    if len(array) < 2:
        return array

    middle = array[0]
    left = [i for i in array[1::] if i <= middle ]
    right = [i for i in array[1::] if i > middle ]
    return quick_sort(left) + [middle] + quick_sort(right)

print(quick_sort([2,5,4,8,1]))


int_a = 12300

list_a = list(str(int_a))
list_a.reverse()

for i in list_a:
    print(i)
    if i == '0':
        list_a.pop(0)
        print(list_a)
    else:
        break

print(list_a)