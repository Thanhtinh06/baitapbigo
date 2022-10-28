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

    def check_number_five(self):
        if self.head == None:
            return None
        else:
            var = 5
            ans = self.head
            while ans != None:
                if ans.data % 10 != var:
                    print(ans.data, end=" ")
                ans = ans.next


lst = LinkedList()
n = int(input())
for i in range(n):
    x = int(input())
    lst.insertTail(x)
lst.check_number_five()
