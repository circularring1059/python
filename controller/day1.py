#if

a = ""
if not a:
    print("这是一个空字符串")

# a = int(input("input:"))   #输入的是字符串

# if a == 1:
#     print("a == 1")
# elif a == 2:
#     print("a ==2")
# else:
#     print("a == other")

#for
for i in "ring":
    print(i)
for i in range(10):
    print(i)
print([i for i in range(10) if i % 2 ==0 ]) #[0, 2, 4, 6, 8]
for i in range(1, 10):
    for j in range(1,i+1):
        print("{}*{}={}".format(j, i, i*j),end="   ")
    print()

for i  in  range(10):
    print(i)
    if i == 10:
        break
else:
    print("no break")

#while
# while True:
#     print("无线循环")
i = 1
while i < 10:
    print(i)
    i += 1

i= 1
while i < 10:
    j = 1
    while j <= i:
        print("{}*{}={}".format(j, i, i*j),end="   ")
        j += 1
    print()
    i += 1

i = 1
while i <= 10:
    i += 1
    print(i)
    if i == 12:
        break
else:
    print("no break")