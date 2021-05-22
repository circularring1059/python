def add():
    def func(x, y):
        return x + y
    return func


addFunc = add()
print(addFunc)
print(addFunc(1,3))
print(addFunc(12,3))

# def line_conf():
#     b = 15
#     def line(x):
#         return 2*x+b
#     return line       # return a function object
#
# b = 5
# my_line = line_conf()
# print(my_line.__closure__)  #(<cell at 0x000002C48CBDD8B8: int object at 0x00007FFCFC30A350>,)
# print(my_line(5))


def line_conf(a, b):
    def line(x):
        return a*x + b
    return line

line1 = line_conf(1, 1)
line2 = line_conf(4, 5)
print(line1(5), line2(5))