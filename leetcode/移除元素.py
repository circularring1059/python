def removeElement(array, val):
    if not len(array):
        return 0
    i = 0
    while i < len(array):
        if array[i] == val:
            array.remove(array[i])
        else:
            i += 1
    return len(array)

print(removeElement([1,234,45,4,5,4], 4))

def removeElement1(array, val):
    if not array:
        return 0

    i = 0
    for j in range(len(array)):
        if array[j] != val:
            array[i] = array[j]
            i += 1
    return i

print(removeElement1([1,2,4,4,5,2,1], 1))

# def removeElement2(array, val):
#     for i in range(len(array)-1, -1, -1):
#        if array[i] == val:
#            array.pop()
#     return array
#
#
# print(removeElement2([1,2,3,3,4],3))