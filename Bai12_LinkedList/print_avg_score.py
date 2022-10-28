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

    def printBlowAvg(self):
        if self.head == None:
            return None
        else:
            var = 5
            ans = self.head
            while ans != None:
                if ans.data < var:
                    if ans.data % 1 != 0:
                        print(ans.data)
                    else:
                        print(int(ans.data))
                ans = ans.next


lst = LinkedList()
while True:
    x = float(input())
    if x == -1:
        break
    lst.insertTail(x)
lst.printBlowAvg()
