a = [1,2,3]

def func(arg):
    b = 1
    print(locals())  #{'arg': 1, 'b': 1}
    print(globals())
    arg.append(4)
    return arg
print(func(a))
print(a)


c = 1
def func(arg):
    b = 1
    print(locals())  #{'arg': 1, 'b': 1}
    print(globals())
    arg += 1
    return arg
print(func(c)) #2
print(c) #1
