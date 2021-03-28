name = "pke.calaulate"

class Calculate:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)


print(__name__)  # import  时为 model.pkg.calculate

def show():
    print("pkg.show")

if __name__ == '__main__':
    show()