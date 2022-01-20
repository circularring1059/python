class Node():
    def __init__(self, elem=-1, left=None, right=None):
        self.elem = elem
        self.left = left
        self.right = right


class Tree():
    def __init__(self, root=None):
        self.root = root

    def add(self, elem):
        node = Node(elem)
        if self.root is None:
            self.root = node
        else:
            queue = []
            queue.append(self.root)
            while queue:
                cur = queue.pop(0)
                if cur.left is None:
                    cur.left = node
                    return
                else:
                    queue.append(cur.left)
                if cur.right is None:
                    cur.right = node
                    return
                else:
                    queue.append(cur.right)

    def breadth_travel(self):
        """层序遍历"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur = queue.pop(0)
            # print("*")
            print(cur.elem, end=" ")
            if cur.left is not None:
                queue.append(cur.left)
            if cur.right is not None:
                queue.append(cur.right)
        print()

    def breadth_travel1(self):
        '''分层存储'''
        if self.root is None:
            return
        queue = [self.root]
        list1 = []
        while queue:
            list2 = []
            for  _  in range(len(queue)):
                cur = queue.pop(0)
                if cur.left is not None:
                    queue.append(cur.left)
                if cur.right is not None:
                    queue.append(cur.right)
                list2.append(cur.elem)
            list1.append(list2)
        return list1

    def breadth_travel2(self):
        '''z 型打印'''
        if  self.root is  None:
            return
        queue = [self.root]
        list1 = []
        i = 0
        while queue:
            list2 = []
            for _ in range(len(queue)):
                cur = queue.pop(0)
                if i % 2 == 0:
                    print("**")
                    list2.append(cur.elem)
                else:
                    list2.insert(0,cur.elem)
                if cur.left is not None:
                    queue.append(cur.left)
                if cur.right is not None:
                    queue.append(cur.right)

            list1.append(list2)
            i += 1

        return list1



    def preorder(self):
        """先序遍历"""
        cur = self.root
        def inner(cur):
            if cur is None:
                return
            print(cur.elem, end=" ")
            inner(cur.left)
            inner(cur.right)

        inner(cur)
        print()

    def inorder(self):
        """中序遍历，二叉搜索树就是按序输出了"""
        cur = self.root
        def inner(cur):
            if cur is None:
                return
            inner(cur.left)
            print(cur.elem, end=" ")
            inner(cur.right)
        inner(cur)
        print()

    def afterorder(self):
        cur = self.root
        def inner(cur):
            if cur is None:
                return
            inner(cur.left)
            inner(cur.right)
            print(cur.elem, end=" ")
        inner(cur)
        print()

    def countOfNode(self):
        cur = self.root
        count = 0
        def inner(cur):
            if cur is None:
                return
            nonlocal count
            count += 1
            inner(cur.left)
            inner(cur.right)

        inner(cur)
        return count
    def kthSmallest(self, k):
        cur = self.root
        ret = []
        def inner(cur):
            if cur is None:
                return
            inner(cur.left)
            ret.append(cur.elem)
            inner(cur.right)

        inner(cur)

        if len(ret) < k or k < 1:
            return None
        return ret[k-1]







tree_instance = Tree()

tree_instance.add(2)
tree_instance.add(1)
tree_instance.add(3)
tree_instance.add(4)
tree_instance.add(5)
# tree_instance.breadth_travel()
# tree_instance.preorder()
# tree_instance.inorder()
# tree_instance.afterorder()
# # print(tree_instance.countOfNode())
# print(tree_instance.kthSmallest(1))
print(tree_instance.breadth_travel1())
print(tree_instance.breadth_travel2())