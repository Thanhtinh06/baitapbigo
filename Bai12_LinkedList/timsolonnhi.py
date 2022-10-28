class Node:
    def __init__(self, x=None):
        self.data = x
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertTail(self, x):
        p = Node(x)
        if (self.head == None):
            self.head = self.tail = p
        else:
            self.tail.next = p
            self.tail = p

    def removeAfter(self, ans, remove):
        ans.next = remove.next
        remove.next = None

    def removeHead(self):
        if self.head.next != None:
            self.head = self.head.next
        else:
            self.head = None

    def removeTail(self):
        cur = self.head
        while cur != None:
            if cur.next == self.tail:
                self.tail.next = cur
                self.tail = cur
                break
            cur = cur.next

    def find_max(self):
        if self.head == None:
            return None
        else:
            ans = self.head
            cur = self.head
            while cur != None:
                if cur.data > ans.data:
                    ans = cur
                cur = cur.next
            return ans

    def find_max_second_number(self):
        max_node = self.find_max()
        cur = self.head

        while cur != None:
            if cur == self.head and cur.data == max_node.data:
                self.removeHead()
            elif cur.next == None and cur.data == max_node.data:
                self.removeTail()
            elif cur.next == None:
                break
            elif cur.next.data == max_node.data:
                self.removeAfter(cur, cur.next)
            cur = cur.next
        return self.find_max()


lst = LinkedList()
while True:
    x = float(input())
    if x == -1:
        break
    lst.insertTail(x)

ans = lst.find_max_second_number()
if ans == None:
    print(-1)
else:
    if ans.data % 1 != 0:
        print(ans.data)
    else:
        print(int(ans.data))
