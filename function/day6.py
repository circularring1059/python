#枚举
li  = ["a", "b", "c", "d"]
str1 = "abcd"
dc = {1:1, 2:2, 3:3, 4:4}

for x, y in enumerate(li):
    print(x, y)

for x, y in enumerate(str1, 2):
    print(x, y)

for x in enumerate(dc, 3):
    print(x)