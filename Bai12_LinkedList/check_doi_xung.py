

class Node:
    def __init__(self, x=None):
        self.data = str(x)
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

    def printSymmetricNumbers(self):
        if self.head == None:
            return None
        else:
            ans = self.head
            count = 0
            while ans != None:
                reverser = ans.data[::-1]
                if ans.data == reverser:
                    print(count, end=" ")
                count += 1
                ans = ans.next


lst = LinkedList()
while True:
    x = int(input())
    if x == -1:
        break
    lst.insertTail(x)
lst.printSymmetricNumbers()
