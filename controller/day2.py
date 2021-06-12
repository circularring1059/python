a = 0
if not a:
    print("a == 0")

s = 1 != 1 or "a" == "a" and "h" in "hello"
print(s)

flag = True
while flag:
    for i in range(10):
        print(i)
        if i == 6:
            flag = False
            break
    else:
        print("XXX")
else:
    print("XXX") #  这个会print