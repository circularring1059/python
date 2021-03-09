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