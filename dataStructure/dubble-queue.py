class DubbleQueue():
    def __init_(self):
        self.__list = []

    def add_front(self, item):
        #头部入队
        self.__list.insert(0, item)

    def add_rear(self, item):
        #尾部入队
        self.__list.append(item)

    def pop_front(self):
        #头部出队
        return self.__list().pop(0) if self.__list() else None

    def pop_rear(self):
        #尾部出队
        return self.__list.pop() if self.__list() else None

    def is_empty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)

if __name__ == '__main__':
    pass