class Node():
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class Student():
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        return self.__head == None

    def length(self):
        cur = self.__head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__head
        while cur != None:
            print(cur.elem, end=' ')
            cur = cur.next
        print("")

    def add(self, item):
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        if pos <= 0:
            self.append((item))
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count < (pos - 1):
                count += 1
                pre = pre.next
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        cur = self.__head
        pre = None
        while cur != None:
            if cur.elem == item:
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == "__main__":
    print("start crud singe linked list")
    sing_list = Student()
    print(sing_list.is_empty())
    sing_list.append(1)
    sing_list.append("one")
    sing_list.append(2)
    sing_list.append("two")
    print(sing_list.length())
    sing_list.travel()
    sing_list.remove("one")
    sing_list.remove("two")
    sing_list.travel()
    sing_list.insert(2, "3")
    sing_list.travel()
    sing_list.add("zero")
    sing_list.travel()
    print(sing_list.search("zero"))





class Linkd():
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        return self.__head == None

    def add(self, item):
        node = {"data":item, "next": None}
        node["next"] = self.__head
        self.__head = node

    def append(self, item):
        node = {"data": item, "next": None}
        if self.is_empty():
            # self.add(self, item)
            self.__head = node
        else:
            cur = self.__head
            while cur["next"] != None:
                cur = cur["next"]
            cur["next"] = node

    def travel(self):
        cur = self.__head
        if cur:
            print(cur.get("data"))
            while cur["next"] != None:
                cur = cur["next"]
                print(cur["data"], end="\n")

    def length(self):
        cur = self.__head
        if not cur:
            return 0
        count = 1
        while cur["next"] != None:
            cur = cur["next"]
            count += 1
        return count


    def insert(self, pos, item):
        pass




link = Linkd()
print(link.is_empty())
link.append(9)
link.add(8)
link.travel()
print("length:", link.length())
print(link.is_empty())