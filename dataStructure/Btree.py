class BTree():
    def __init_(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    #先序遍历
    def preorder(self):
        if self.data is not None:
            print(self.data, end= "")
        if self.left is not None:
            self.left.preorder()
        if  self.right is not None:
            self.right.preorder()
    #中序遍历
    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        if self.data is not None:
            print(self.data)
        if self.right is not None:
            self.right.inorder()

    #后序遍历
    def postorder(self):
        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        if self.data is not None:
            print(self.data)

    #树高
    def high(self):
        if self.data is None:
            return 0
        elif self.left is None  and self.right is None:
            return 1
        elif self.left is None  and self.right is not None:
            return 1 + self.right.high()
        elif self.left is not None and self.right is None:
            return 1 + self.left.high()
        else:
            return 1 + max(self.left.high(), self.right.high())

    #叶子节点
    def leaves(self):
        if self.data is None:
            return None
        elif self.left is None and self.right is None:
            print(self.data, end="")
        elif self.left is None and self.right is not None:
            self.right.leaves()
        elif self.left is not None and self.right is None:
            self.left.leaves()
        else:
            self.left.leaves()
            self.right.leaves()


    def levelorder(self):
        #左孩子
        def LChild_Of_Node(node):
            return node.left if node.left else None
        #右孩子
        def RChild_Of_Node(node):
            return node.right if node.right else None
        #层序遍历列表
        level_order  = []
        if self.data:
            level_order.append([self])

        #高度
        high = self.high()
        if high >= 1:
            for _ in range(2, high + 1):
                level = []
                for node in level_order[-1]:
                    if LChild_Of_Node(node):
                        level.append(LChild_Of_Node(node))
                    if RChild_Of_Node(node):
                        level.append(RChild_Of_Node(node))
                if level:
                    level_order.append(level)







