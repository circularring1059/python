"""单例模式"""


class Person:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)

        return cls.__instance

person1 = Person()

person2 = Person()

print(person1, person2)