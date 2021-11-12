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





