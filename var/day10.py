from functools import reduce

listA = [1,2,3,4,2,3,1,1]


def  Soultion(nums):
    return reduce(lambda  x,y: x if y in x else x +[y], [[],] + nums )

listA = Soultion(listA)

print(listA)



dictB = {}.fromkeys([1,3,2,3,4,5,5])
print(dictB)
print(list(dictB.keys()))
print(list(dictB.values()))

for i in dictB.items():
    print(i)


dictA = {"one":1, "two":2}
print(dictA.setdefault("three", 3))
print(dictA)

print(list(set([1,2,3,4,3])))


listC = [1,3,3,4,5,5]
print(listC[-1:0:-1])
for i in range(len(listC)-1, -1, -1):
    print(i)
    if listC[i] == 5:
        # listC.pop(i)
        listC.remove(listC[i])
print(listC)

