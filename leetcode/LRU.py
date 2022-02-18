class Node():
    def __init__(self, key = None, value= None, ):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRU():
    def __init(self, capacity:int ):
        self.capacity = capacity
        self.hashmap = {}
        self.head   = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def move_node_to_tail(self, key):
        if key not in self.hashmap:
            return
        node = self.hashmap[key]
        print(node.value)

        node.prev.next = node.next
        node.next.prev = node.prev

        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.hasmap:
            self.move_node_to_tail(key)
            return self.hasmap[key].value
        else:
            return -1

    def put(self, key:int, value: int) -> None:
        if key in self.hasmap:
            self.hasmap.pop(self.head.next.key)
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
        new = Node(key, value)
        self.hasmap[key] = new
        new.prev = self.tail.prev
        new.next = self.tail
        self.tail.prev.next = new
        self.tail.prev = new
