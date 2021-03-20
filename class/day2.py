class Person():
    brand = "txy"
    num = 34
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.num = Person.num  #self.num = num  error

    def __onot__(self):
        print("hello")


    def fun(self, arg):
        self.name += arg
        print(arg, self.brand)
        print(self.name)

    def show(self):
        print(Person.num)
        print(self.num)

person1 = Person("xiaoming", 19)

print(person1.age) # 18
print(person1.name) # xiaoming
person1.__onot__() # hello
person1.fun("hell0 class")  # hell0 class txy


Person.name = "class"
print(Person.name) # class


person2 = Person("xiaojing", 11)
print(person2.num)  # 34
person2.num += 1
print(person2.num) # 35
person2.show() #34 35