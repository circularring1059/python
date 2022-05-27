def isRing(node):
    if node is None or node.node is None or node.node.node is None:
        return False

    one_node = node
    two_node = node
    while two_node.node is not None:
        one_node = one_node.node
        two_node = two_node.node.node

        if two_node is None:
            return False
        if two_node == one_node or two_node.node == one_node:
            return True
    return False


class Node():
    def __init__(self, value, node=None):
        self.value = value
        self.node = node



node1 = Node(1)
node2 = Node(2)
# node3 = Node(3)

node1.node = node2
# node2.node = node3

print(isRing(node1))

# node3.node = node3
node2.node = node1
print(isRing(node1))
