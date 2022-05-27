class A:
    def method(self):
      print("CommonA")
class B(A):
    print("commonB")
class C(A):
    def method(self):
      print("CommonC")
class E:
    pass
class D(B, C,E):
    pass

# print(D.__mro__)  #(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class '__main__.E'>, <class 'object'>)
d = D()
d.method()  #commonB CommonC
# print(D().method())