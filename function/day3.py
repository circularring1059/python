#匿名函数
func = lambda x,y: x + y
print(func(1,3)) #4


#列表排序
li1 = ["a", "ab", "abc", "abcd"]
li1.sort(key=lambda item:len(item), reverse=True)
print(li1)

#字典排序
dc1 = {"a:": 100, "b": 50, "c": 79}
dc1Item = dc1.items()
dc1_sort = sorted(dc1Item, key=lambda item:item[1])
print(dc1_sort)