#多元赋值
a, b, c = 1, 2, 3
print(a, b, c) #1 2 3
*a, b, c = 1, 2, 3, 4, 5
print(a) #[1, 2, 3]
*_, b, c = 1, 2, 3, 4, 5
print(_) #[1, 2, 3]

str1 = "ring"

a, b, c, d = str1
print(a, b, c, d) # r i n g

#列表 元组 。。。  也是一样的(可迭代）
a, b, c =[1, 2, 3]
a, b, c =(1, 2, 3)
a, b, c ={1, 2, 3}
a, b, c ={1:1, 2:2, 3:3}
print(a, b, c)