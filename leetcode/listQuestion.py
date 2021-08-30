"""
input [1,2,3]
output [[1,2,3],[2,3,1],[3,1,2]]
"""
import copy


def listFun(array):
    listA = []
    listA.append(array)
    for i in range(len(array)-1):
        # tem_list = listA[i].copy()
        tem_list = copy.deepcopy(listA[i])
        tem_list.append(tem_list.pop(0))
        listA.append(tem_list)

    return listA

print(listFun([1,2,3,4]))
print(listFun([1,2,3,4,5]))


def func(arrary):
    res = []
    res.append(arrary)
    for i in range(len(arrary)-1):
        tmp_tuple = tuple(res[i])
        tmp_list = list(tmp_tuple)
        tmp_list.append(tmp_list.pop(0))
        res.append(tmp_list)
    return(res)

print(func([1, 2, 3]))