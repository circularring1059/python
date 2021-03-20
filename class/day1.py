class Person:
    tall = 168

person1 = Person()

print(person1.tall) # 168

person1.tall= 169

print(person1.tall) # 169

person2 = Person()

print(person2.tall) # 168

Person.tall = 188

person3 = Person()

print(person3.tall) # 188

print(person2.tall) # 188

print(person1.tall) # 169


class Phone:
    message = ""
    def fun(self):
        print(self)
        print(self.message)

iphone = Phone()
print(iphone)  # <__main__.Phone object at 0x00000263F7BFA948>
iphone.fun() # <__main__.Phone object at 0x00000263F7BFA948>


aphone = Phone()
aphone.message = "hello aphone"
aphone.fun() # hello aphone
print(aphone.message) # hello aphone