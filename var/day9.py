#zip

li1 = ["a", "b", "c"]
li2 = [1, 2, 3, 4]

zip1 = zip(li1, li2) #<zip object at 0x000002404890F448>

print(zip1)
for x, y in zip1:
    """
    a 1
    b 2
    c 3
    """
    print(x, y)

for item in zip([1,2, 3], [1, 2, 3]):
    print(item)
    x, y = item
    print(x, y)

print(list(zip(["1",2,3], [1, 2, 3, 4]))) #[('1', 1), (2, 2), (3, 3)]
print(list(zip((1,2,3), [1, 2, 3, 4]))) #[(1, 1), (2, 2), (3, 3)]
print(list(zip("abc", [1, 2, 3, 4]))) #[(1, 1), (2, 2), (3, 3)]  可迭代就可以