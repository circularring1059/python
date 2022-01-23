class Node():
    def __init__(self,elem=None, node=None):
        self.elem = elem
        self.node = node

def isLoop(node):
    if node is None or node.node is None:
        return False
    slow = node
    fast = node
    while fast is not None and fast.node is not None:
        slow = slow.node
        fast = fast.node.node
        if slow == fast:
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
node1 = Node(1, node2)  #有环
print(isLoop(node4))