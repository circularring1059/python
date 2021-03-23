"""
面向对象交互
"""

class Sutent:
    def __init__(self, name, book):
        self.name = name
        # self.book = []
        # self.book.append(book)
        self.book = [str(book)]
        self.book = book

    def showMybook(self):
        return self.book

    def __str__(self):
        return "stdent's name:{}".format(self.name)

    def  borrowBook(self,book):
        for book1 in self.book:
            if book1  == book.name:
                break
        else:
            self.book.append(book)
            print("borrow book name:{}".format(book.name))

class Book:
    def __init__(self, name, author, num):
        self.name = name
        self.author = author
        self.num = num

    def __str__(self):
        return "book's name:{}".format(self.name)

student = Sutent("jack","mysql")

book = Book("kubernetes", "nonknow", 9)


# student.borrowBook(book)
# print(student.showMybook())


student1 = Sutent("cat", book)
print(student1.book)  # book's name:kubernetes
print(student1.showMybook()) # book's name:kubernetes

