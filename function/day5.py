#装饰器


def func1(f):
    def inner():
        print("装饰前")
        f()
        print("装饰后")
    return inner
@func1
def func():
    print("hello world")

# func = func1(func)
# func()
func()  #语法糖


