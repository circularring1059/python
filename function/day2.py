def  add(x, y):
    return x + y

print(add(1,2))
print(eval("add(2,3)"))


#参数
def func(x,y, *args, **kwargs):
    return x, y, args, kwargs

print(func(1,3,3,4,a=1,b=2)) #(1, (3, 4, 3, 4), {'a': 1, 'b': 2})

def func(x,y=5, *args, **kwargs):
    return x, y, args, kwargs
print(func(1,a=1,b=2)) #(1, 5, (), {'a': 1, 'b': 2})


#global
a = 1
def changeA():
    global a
    a = a + 1
changeA()
print(a)  #2

li = [1, 2, 3]
def changeLi():
    li.append(4)
changeLi()
print(li)

#local
def out():
    b = 2
    def inF():
        nonlocal b
        b = b +1
    inF()
    print(b)
out()


dc = {"1":"1", "2":"2"}
li1 = [1, 2, 3]
def func(*args, **kwargs):
    print(args, kwargs)
func(*li1, **dc) #(1, 2, 3) {'1': '1', '2': '2'}