import random

print(random.random()) #0 到1 之间的小数

print(random.randint(1, 10))  #闭区间  没有步长

print(random.randrange(1, 10, step=2))  #开区间  支持步长

str1 = "circularring1010"
list1 = [1, 2, 5]
tuple1 = (1, 5, 8)
print(random.choices(str1)) #返回列表
print(random.choices(list1)) #返回列表
print(random.choices(tuple1))  #返回列表


list2 = [1, 4, 5, 0]
random.shuffle(list2) #打乱列表顺序
print(list2)

#随机产生A ~ Z
print(chr(random.randint(65,90)), type(chr(random.randint(65,90))))
