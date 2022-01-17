class Node():
    def __str__(self,elem=-1, left=None, right=None):
        self.elem = elem
        self.left = left
        self.right = right


class Tree():
    def __init__(self, root=Node):
        self.root = root

    def add(self, elem):
        node = Node(elem)
        if self.root:
            self.root = node
        else:
            queue = []
            queue.append(self.root)
            while queue:
                cur = queue.pop(0)
                if cur.left == None:
                    cur.left = node
                    return
                elif cur.right == None:
                    cur.right = node
                    return
                else:
                    queue.append(cur.left)
                    queue.append(cur.right)
