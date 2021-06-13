a = 1
b = "ring"
c = True
d = 1.01

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

d =  300
print(d, id(d)) #300 2467493753904
e =  300
f = e
print(e,id(e)) #300 2467493753904
print(f,id(f)) #300 2467493753904

# a = input()
# b = input()
# print(a, id(a)) #12 2697012408880
# print(b, id(b)) #12 2697008771120

a = 1
b = a  #引用传递
a = 2
print(a, b) #2 1
# 内置关键字
import keyword
print(keyword.kwlist)

isKeyW = keyword.iskeyword("del")
print(isKeyW)  #True