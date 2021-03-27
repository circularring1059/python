class Person:
    def __init__(self):
        self.__name = "匿名"

    def show(self):
        print(self.__name)

    def run(self):
        print("run1")
    # 方法重写
    def run(self,arg):
        print(arg)

person = Person()

# person.run() # error
person.run("hello")

class Student(Person):
    def __init__(self):
        super(Student, self).__init__()
        self.__name = "小明"

    def run(self, arg, suId):
        #继承父类方法并改写
        super(Student, self).run(arg)
        print(suId)

    def show(self):
        super(Student, self).show() # 匿名
        print(self.__name) #小明

xiaoming = Student()
xiaoming.run("run",118)
xiaoming.show()

"""多继承"""

"""python2 分经典类和新新式类， 经典类遵循从左到右，深度优先原则，新式类遵循广度优先原则，
python3中不区分，遵循广度优先原则"""

import inspect

print(Student.__mro__)
print(inspect.getmro(Student))