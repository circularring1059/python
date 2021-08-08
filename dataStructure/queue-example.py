class QueueExample():
    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        #入队
        self.__list.append(item)

    def dequeue(self):
        #出队
        return self.__list.pop(0) if self.__list else None

    def is_empyt(self):
        return self.__list == []

    def size(self):
        return len(self.__list)

if __name__ == '__main__':
    queue_example = QueueExample()
    queue_example.enqueue(1)
    queue_example.enqueue(2)
    queue_example.enqueue(3)
    queue_example.enqueue(4)
    print(queue_example.is_empyt())
    print(queue_example.size())
    print(queue_example.dequeue())
    print(queue_example.dequeue())
    print(queue_example.dequeue())
    print(queue_example.dequeue())
    print(queue_example.dequeue())
    print(queue_example.dequeue())
    print(queue_example.dequeue())