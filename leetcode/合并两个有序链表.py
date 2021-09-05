class Link():
    def __init__(self, node=None):
        self.__head = node

     #头插法
    def add(self, item):
        node = {"data": item, "next":None}
        node["next"] = self.__head
        self.__head = node

    #尾插法
    def append(self, item):
        cur = self.__head
        node = {"data":item, "next":None}
        if cur:
            while cur["next"]:
                cur = cur["next"]
            cur["next"] = node

    def show_head(self):
        print(self.__head)

    #判断空链表
    def is_empty(self):
        return self.__head == None


link1 = Link()
link1.add(1)
link1.append(2)
link1.append(6)
link1.show_head()
print(link1.is_empty())

link2= Link()
link2.add(3)
link2.add(1)
link2.append(5)
link2.show_head()
print(link2.is_empty())


class MergeLink():
    def __init__(self):
        self.__head = None

    def mergeLink(self, link1, link2):
        pre = None
        # if link1.is_empty or link2.is_empty:
        #     pre = link2 if link1.is_empty else link1
        #
        while not link1.is_empty and not link2.is_empty():
            pass
            
