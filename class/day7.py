"""继承"""

class Person:

    __cl = "class"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #定义私有方法
    def __run(self):
        return "{} is running".format(self.name)

    #定义公用方法调用私有变量和方法
    def public(self):
        print(Person.__cl)
        return \
            self.__run()

class Doctor(Person):
    def show(self):
        pass
        # print(Doctor.__cl)  # error  has no attribute '_Doctor__cl'
        # print(Person.__cl)  # error  has no attribute '_Doctor__cl'
        # print(self.__cl)  # error  has no attribute '_Doctor__cl'

doctor = Doctor("jakc", 12)

# print(doctor.__c) # error

doctor.show()

# doctor.__run() # error
# doctor._Doctor.__run()  #  error has no attribute '_Doctor'
# doctor._Person.__run()  #  error has no attribute '_Person'

print(doctor.public())