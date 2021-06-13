#字典
#key 必须是可hash  de
print(hash(1))
# print(hash([1])) #不可hash  报错
dc1 = {1:1, 2:"2", "ring":"yuan"}
print(dc1)

#重复的key 取后面的
dc2 = {1:1, 2:"2", "ring":"yuan", 1:"1"}
print(dc2)

dc3 = {
    1: 2,
    3: 4,
    "one": "four",
}
print(dc3)

#遍历key
for i in dc2:
    print(i)

#字典生成
print(dict(["a1", "b2", "cc", (1,2), [3, 4], {"ring": "ring", "yaun": "yaung"}])) #列表元素可迭代且length为2
print(dict(("a1", "b2", "cc", (1,2), [3, 4], {"ring": "ring", "yaun": "yaung"}))) #列表元素可迭代且length为2
print(dict(a="a1", b="b2"))
print(dict(zip([1,2,3], [1,2,3]))) #{1: 1, 2: 2, 3: 3}

dc4 = dict(["a1", "b2", "cc", (1,2), [3, 4], {"ring": "ring", "yaun": "yaung"}])
print(dc4)
#get value
print(dc4["a"]) #1
# print(dc4["d"]) # 不存在的key  报错
#使用get
print(dc4.get("d")) #不存在的key  返回None
print(dc4.get("e", "key not exist")) #key not exist

#获取key
print(dc4.keys())
#获取value
print(dc4.values())
#获取所有
print(dc4.items())
for  x, y in dc4.items():
    print(x, y)

#修改字典
dc5 = {1:1, 2:2, 3:3}
dc5[0] = "zero"  #增加一个 k -v
print(dc5)
dc5[1] = "one" #修改
print(dc5)
dc5.update({2: "two", 4:4}) #修改
print(dc5)
print(dc5.setdefault(1,"oneone")) #存在key get  value    不存在key   set  k-v
print(dc5.setdefault(5, "five"))
print(dc5) #{1: 'one', 2: 'two', 3: 3, 0: 'zero', 4: 4, 5: 'five'}

#合并两字典
dc6 = {1:1, 2:2}
dc7 = {3:3, 4:4}
dc8 = {**dc7, **dc6}
print(dc8)  #若存在相同key   后者覆盖前者

#删除
dc9 = {1:1, 2:2, 3:3, 4:4}
del dc9[1]  #删除1:1
print(dc9)

print(dc9.pop(2))  #返回删除的value，必须指明key
print(dc9)

print(dc9.popitem())  #返回最后一对，不加参数
print(dc9)

dc9.clear() #清空字典
print(dc9)

# print(dc9.pop(1)) #返回最后一对，
# print(dc9) #'popitem(): dictionary is empty'
#
# print(dc9.popitem()) #返回最后一对，
# print(dc9) #'popitem(): dictionary is empty'

del dc9 #删除整个字典对象
# print(id(dc9)) 报错