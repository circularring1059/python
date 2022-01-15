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

    def index(self, index):
        if self.is_empty():
            return None
        if index >= self.length():
            return "out of index"
        if index == 0:
            return self.__head
        cur = self.__head
        for i in range(index):
            cur = cur.next
        return cur

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


# if __name__ == "__main__":
#     print("start crud singe linked list")
#     sing_list = Student()
#     print(sing_list.is_empty())
#     sing_list.append(1)
#     sing_list.append("one")
#     sing_list.append(2)
#     sing_list.append("two")
#     print(sing_list.length())
#     sing_list.travel()
#     sing_list.remove("one")
#     sing_list.remove("two")
#     sing_list.travel()
#     sing_list.insert(2, "3")
#     sing_list.travel()
#     sing_list.add("zero")
#     sing_list.travel()
#     print(sing_list.search("zero"))


class Linkd():
    def __init__(self, node=None):
        self.__head = node

    def showSelf(self):
        print(self.__head)

    def is_empty(self):
        return self.__head == None

    def length(self):
        cur = self.__head
        if not cur:
            return 0
        count = 1
        while cur["next"] != None:
            cur = cur["next"]
            count += 1
        return count

    def swap(self, indexOne, indexTwo):
        if indexOne < 0 or indexTwo < 0:
            print("index out of range")
            return ""
        if indexOne >= self.length() or indexTwo >= self.length():
            print("index out of range")
            return ""
        if indexOne == indexTwo or self.is_empty() or self.length() == 1:
            pass
        else:
            if self.length() == 2:
                self.reverse()
            else:
                indexOne_data = self.index(indexOne)
                indexTwo_data = self.index(indexTwo)
                cur = self.__head
                for i in range(max(indexOne, indexTwo) + 1):
                    print(i)
                    if i == indexOne:
                        cur["data"] = indexTwo_data
                    if i == indexTwo:
                        cur["data"] = indexOne_data
                    cur = cur["next"]

    def add(self, item):
        node = {"data": item, "next": None}
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

    def index(self, index):
        if self.is_empty():
            return None
        if index >= self.length():
            return "out of index"
        if index == 0:
            return self.__head["data"]
        cur = self.__head
        for _ in range(index):
            cur = cur["next"]
        return cur["data"]

    def travel(self):
        cur = self.__head
        if cur:
            print(cur.get("data"))
            while cur["next"] != None:
                cur = cur["next"]
                print(cur["data"], end="\n")

    def insert(self, pos, item):
        count = 1
        cur = self.__head
        node = {"data": item, "next": None}
        if pos <= 1:
            self.add(item)
        elif pos > self.length():
            self.append(item)
        else:
            while cur["next"] != None:
                count += 1
                if count == pos:
                    node["next"] = cur["next"]
                    cur["next"] = node
                    break

    def remove(self, item):
        cur = self.__head
        if cur["data"] == item:
            self.__head = cur["next"]
        else:
            while cur["next"] != None:
                cur_next = cur["next"]
                if cur_next["data"] == item:
                    cur["next"] = cur_next["next"]
                    break
                cur = cur_next

    def search(self, item):
        cur = self.__head
        if cur["data"] == item:
            return True
        else:
            while cur["next"]:
                cur = cur["next"]
                if cur["data"] == item:
                    return True
            return False

    def reverse(self):
        cur = self.__head
        if cur:
            pre = None
            while cur["next"]:
                next = cur["next"]
                cur["next"] = pre
                pre = cur
                cur = next
            cur["next"] = pre
            self.__head = cur


link = Linkd()
# print(link.is_empty())
# link.append(9)
link.add(8)
link.add(7)
link.add(3)
link.add(1)
# link.insert(2, 6)
# link.insert(2, 1)
# link.remove(7)
# link.travel()
# print("length:", link.length())
# print(link.search(8))
# print(link.is_empty())
# link.travel()
# link.reverse()
# link.travel()
print(link.index(1))
print(link.index(0))
link.showSelf()
link.swap(1, 3)
link.showSelf()
