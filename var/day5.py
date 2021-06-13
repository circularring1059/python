#lsit
li1 = []

li2 = [1, 2, "ring"]
print(li2)

li3 = list("ring")
print(li3) #['r', 'i', 'n', 'g']
print(list((1, 2, 3,)))  #可迭代都行
print(list({1:1, 2:2, 3:3}))

print([i for i in range(10) if i %2 ==0])  #[0, 2, 4, 6, 8]
print([x+y for x in "ring" for y in 'yuan' if x != "g" if y != "u" ])

#切割 同string
print(li2[0:2])

#赋值 引用传递
li4 = li2
print(id(li2), id(li2)) #2936122528648 2936122528648

li5 = list(li2)
print(id(li2), id(li2)) #2936122528648 2936122528648

li20 = li2[:]
print(id(li20), id(li2))
print('*****')
#copy 浅拷贝
li6 = li2.copy()
print(id(li6), id(li2)) #3108727257864 3108719907720

li7 =[1, 2, [1, 2]]
li8 = li7.copy()
print(li8)
li7[1] = "one"
li7[2][1] = "one"
print(li8) # [1, 2, [1, 'one']] 里面一层变，外层不变

#deepcopy
import copy
li9 = li7 =[1, 2, [1, 2]]
li10 = copy.deepcopy(li9)
print(li10)
li9[1] = "one"
li9[2][1] = "one"
print(li10) #不会改变

#for 遍历
for i in li10:
    if isinstance(i, list):
        for j in i:
            print(j)
        continue
    print(i)

#insert
li11 = [1, 2, 3]
li11.insert(0,0)
print(li11) #[0, 1, 2, 3]

#in
print(1 in li11) # True

#append
li12 = [1, 2, 3]
li12.append(4)
print(li12) #[1, 2, 3, 4]

#pop
li13 = [1, 2, 3]
li13_pop = li13.pop()  #默认最后一个
print(li13_pop, li13) #3 [1, 2]
li13_pop = li13.pop(0)
print(li13_pop, li13)

#remove
li14 = [1, 2, 3, 3]
li14.remove(3) #只会remove 一个
print(li14)

#sort
li15 = [2, 1, 3]
li15.sort()
print(li15)


#reverse
li16 = [1, 2, 3]
li16.reverse()
print(li16)


#len
li17 = [1, 2, 3]
print(len(li17))

#count
li18 = [1, 2, 3]
print(li18.count(3))

#extend
li19 = [1, 2, 3]
li19.extend([4, 5, 6])
print(li19)
li19.extend("ring")
print(li19) #[1, 2, 3, 4, 5, 6, 'r', 'i', 'n', 'g']

#join
li20 = ["1", "2", "3"]
st1 = "".join(li20)
print(st1, type(st1)) #str class