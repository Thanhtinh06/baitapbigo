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

    def min(self):
        if (self.head == None):
            return None
        else:
            ans = self.head
            cur = self.head
            while cur != None:
                if cur.data < ans.data:
                    ans = cur
                cur = cur.next
            return ans


lst = LinkedList()
while True:
    x = int(input())
    if x == 0:
        break
    lst.insertTail(x)
ans = lst.min()
print(ans.data)
