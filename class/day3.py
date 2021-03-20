class Person:
    cl = "class"
    def __init__(self, name, age):  #魔术方法
        self.name = name
        self.age = age

    def __str__(self):
        return(self.name)

    def __call__(self, *args, **kwargs):
        print(self.name, *args)

    def __del__(self):
        print("实例被销毁，内存释放")

    def fun(self, num):
        print(self.name, num)

    def fun1(self, number):
        self.fun(number)

    @staticmethod
    def static_fun():
        print("我是静态方法")


person = Person("circularring1010","25")

#对象调用类属性
print(person.cl)
#类调用类属性
print(Person.cl)

person.cl = "person_class"
print(person.cl)  # person_class
print(Person.cl)  # class


#调用__str__方法
print(person)

person("调用__call__方法")

person.fun1(99)

#对象调用静态方法
person.static_fun()

#类调用静态方法
Person.static_fun()