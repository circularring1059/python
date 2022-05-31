class Node():
    _instance = None


    def __init__(self,elem=None, node=None):
        self.elem = elem
        self.node = node

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(Node, "_instance"):
            Node._instance = Node(*args, **kwargs)
        return Node._instance

def isLoop(node):
    if node is None or node.node is None:
        return False
    slow = node
    fast = node
    while fast.node is not None:
        slow = slow.node
        fast = fast.node.node
        if fast is None:
            return False
        if slow == fast or slow == fast.node :
            return True


    return False



#构造链表

# node1 = Node(1,)
# node2 = Node(2,node1)
# node3 = Node(3, node2)
# node4 = Node(4, node3)

# 4->3->2->1  无环
# print(isLoop(node4))

node1 = Node(1,)
node2 = Node(2,node1)
node3 = Node(3, node2)
node4 = Node(4, node3)
# node1.node = node3  #有环
print(isLoop(node4))
