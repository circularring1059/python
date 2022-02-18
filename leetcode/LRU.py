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