"""继承"""

class Person:
    cl = "class"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print("{} is running".format(self.name))

    def __str__(self):
        return self.name

class Student(Person):
    def __init__(self,name, age, stuId):
        super(Student, self).__init__(name, age)
        self.stuId = stuId

    def watchBook(self):
        print("{} is reading book".format(self.name))

    def __str__(self):
        return self.name+str(self.stuId)

student = Student("xiaohonng", 18, 1010)

print(student.stuId)
#调用父类方法
student.run()

#调用自己的方法
student.watchBook()

#重写父类方法(__str__)
print(student)

print(student.cl)