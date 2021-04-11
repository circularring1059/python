class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def showSelf(self):
        print(self.name, self.age)


class Docter(Person):
    def __init__(self, name, age):
        super(Docter, self).__init__(name, age)
        self.name = name

ring = Docter("ring", 18)
ring.showSelf()