def choose_sort(arg):
    for i in range(len(arg)-1):
        middle = i
        for y in range(i+1,len(arg)):
            if arg[middle]  >  arg[y]:
                middle = y
        arg[i],arg[middle] = arg[middle],arg[i]
    return arg


class ChooseSort():
    def choose_sort(self, array):
        if len(array) < 2:
            return array

        for i in range(len(array)-1):
            middle = i
            for y in range(i+1, len(array)):
                if array[middle] > array[y]:
                    middle = y
            array[i], array[middle] = array[middle], array[i]
        return array



choose = ChooseSort()
print(choose.choose_sort([2,4,1,8,3]))
