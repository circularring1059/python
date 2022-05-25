from functools import reduce

listA = [1, 2, 3, 4]

listB = list(filter(lambda x : x != 2, listA))

print(listB) #[1, 3, 4]


listC = [1, 2, 3]
listD = list(map(lambda x : x*2, listC))
print(listD) #[2, 4, 6]

listH = [ 1, 2, 3, 4, 1]

listF = reduce(lambda x, y: x if y in x else x +[y], [[],] + listH)
x = reduce(lambda x, y: x+y, listH)
print(list(listF))
print(x)


a = [ i % 2 for i in range(10)]
b =  ( i % 2 for i in range(10) )
print(a, b)
print(int(9 / 2))