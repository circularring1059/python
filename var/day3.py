#整型
a = 1
b = 0xa
c = 0b0101
print(a, b, c) #1 10 5
d = "1.99"
# print(int(d)) err

#浮点数
a = 0.01
print(type(a))   #<class 'float'>
b = 1
print(float(b)) #1.0
del b  #删除 b引用
# print(b)  报错 name 'b' is not defined
