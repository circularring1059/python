#元组
tp1 = 1,2,3,
print(tp1)

tp2 = 1,
print(tp2)

tp3 = (1)
print(tp3, type(tp3)) #1 <class 'int'>

tp4 = (1, 2, 3)
print(tp4)

from collections.abc import Iterable
# import collections
print(isinstance(tp4, Iterable))  #可迭代的

li = [1, 2, 3]
tp5 = tuple(li)
print(tp5)

print(tuple("ring")) #('r', 'i', 'n', 'g')

#切片取值同列表
print(tp4[1])
print(tp4[:1]) #(1,)


#join
print("".join(("1", "2", "3")))  #里面的元素需要全为str

#相对不可变

li = [1, 2, 3]
tp6 = (1, 2, 3, li)
print(tp6, id(tp6)) #(1, 2, 3, [1, 2, 3]) 1820092513160
li.pop()
print(tp6, id(tp6)) #(1, 2, 3, [1, 2]) 1820092513160

#解包
a, *b = (1, 2, 3)
print(a, b) #1 [2, 3]