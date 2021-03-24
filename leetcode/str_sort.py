def com_str(str1, str2):
    i = 0
    while i < len(str1) and i < len(str2):
        if str1[i] > str2[i]:
            return False

        if str1[i] < str2[i]:
            return True
        else:
            i += 1

    if len(str1) == i:
        return True
    else:
        return False


#  这里用冒泡排序，快排，选排也一样的
def str_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1 - i):
            if com_str(array[j], array[j + 1]):
                # 逆序
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
