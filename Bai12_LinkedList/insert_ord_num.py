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
        if self.head == None:
            self.head = self.tail = p
        else:
            self.tail.next = p
            self.tail = p

    def insert_ord_num(self):
        p = Node(1)
        p.next = self.head
        self.head = p
        cur = p.next
        i = 2
        while cur.next != None:
            t = Node(i)
            t.next = cur.next
            cur.next = t
            cur = t.next
            i += 1


lst = LinkedList()
while True:
    x = int(input())
    if x == 0:
        break
    lst.insertTail(x)

lst.insert_ord_num()
ans = lst.head
while ans != None:
    print(ans.data, end=" ")
    ans = ans.next
