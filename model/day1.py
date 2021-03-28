"""模块"""
#限制import * 里面的内容
# __all__ = ["name", "number"]


name = "circularring1010"
number = "100"

def add(*args):
    return sum(args)


def test():
    print("非import")

class Calculate:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("calculation:{}".format(self.name))

    @classmethod
    def show1(cls):
        print("类方法")


print(__name__)  # 在非调用时__name__ = "__main__", 被import 引入时__name__ = "model.day1"

if __name__ == '__main__':
    test()