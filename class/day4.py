class Person:
    __cl = "class"  #私有
    def __init__(self, name, age):
        self.__cl = Person.__cl
        self.__name = name
        self.__age = age

    def __privateFun(self):
        print("我是私有方法")

    def getName(self):
        print(self.__name)
        print(self.__cl)


person = Person("circularring1010", 26)

#调用私有类属性
#print( Person.__cl)  # error
print(Person._Person__cl) # class

# print(person.__cl) #error
print(person._Person__cl) #class

# print(person.__name) #error
print(person._Person__name) # circularring1010
print(person._Person__cl) # class

# person.__privateFun() #error
person._Person__privateFun() # 我是私有方法

#调用内部方法拿到私有属性
person.getName() # circularring1010 class

person.__cource = 100
person.__cl = "perseonClass"
print(person.__cource) # 100
print(person.__cl)  # personCl
print("*" * 8)
person.getName() # 注意这里__cl=class  而不personClass

print(dir(Person)) #获取类的属性
print(dir(person)) #获取对象的属性  私有属性可以通过_class__** 访问