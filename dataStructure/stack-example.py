class Stack():
    def __init__(self):
        self.__list = []

    def push(self, item):
        #入栈
        self.__list.append(item)

    def pop(self):
        #出栈
        return self.__list.pop() if self.__list else None

    def peek(self):
        #栈顶
        return self.__list[-1] if self.__list else None

    def is_empty(self):
        return self.__list == []
        # return not self.__list

    def size(self):
        return len(self.__list)

if __name__ == '__main__':
    stack_example = Stack()
    stack_example.push(1)
    stack_example.push(2)
    stack_example.push(3)
    print(stack_example.size())
    print(stack_example.peek())
    print(stack_example.pop())
    print(stack_example.pop())
    print(stack_example.pop())
    print(stack_example.pop())
    print(stack_example.pop())
    print(stack_example.pop())