class Node():
    def __init__(self, val, node=None):
        self.val = val
        self.node = node

    def travel(self):
        cur = self.node
        print(self.val)
        while cur:
            print(cur.val)
            cur = cur.node



def Solution(node):
    if node is None or node.node is None:
        return node
    else:
        tmp_node = None
        while node :
            #先获取下一个节点
            next_node = node.node
            #改变当前节点的指向
            node.node = tmp_node
            #tmp_node  变成当前节点
            tmp_node = node
            node = next_node
        return tmp_node


def Solution1(node):
    if not node.node:
        return node

    def backtack(node):
        if not node.node:
            return node
        else:
            newNode = backtack(node.node)
            node.node.node = node
            node.node = None
        return newNode
    node = backtack(node)
    return node





node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.node = node2
node2.node = node3
node3.node = node4
node4.node = node5

# node1.travel()
node_res = Solution1(node1)
node_res.travel()


