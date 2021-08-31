def bubbling_sort(arg):
    for i in range(len(arg) - 1):
        for y in range(len(arg) - i - 1):
            if arg[y] > arg[y + 1]:
                arg[y], arg[y + 1] = arg[y + 1], arg[y]
    return arg

#优化  设置一个flag  在某轮排序后 falg 仍然为 True， 说明无需再排序了

class BubblingSort():
    def __init__(self, array):
        self.array = array

    def bubbling_sort(self):
        for i in range(len(self.array)-1):
            flag =True
            for j in range(len(self.array)-1-i):
                if self.array[j] > self.array[j+1]:
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
                    flag = False
            if flag:
                break
        return self.array

bubbling_sort_ins = BubblingSort([2,5,2,9,6])
print(bubbling_sort_ins.bubbling_sort())