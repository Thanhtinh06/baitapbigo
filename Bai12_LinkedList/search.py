class Value:
    def __init__(self, isRemove, value):
        self.isRemove = isRemove
        self.value = value


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

    def removeHead(self):
        if self.head == None:
            return
        if self.head.next != None:
            self.head = self.head.next
        else:
            self.head = None


lst = LinkedList()
n = int(input())
for i in range(n):
    line = input().split()
    if len(line) == 2 and int(line[0]) == 1:
        value = Value(int(line[0]), int(line[1]))
        lst.insertTail(value)
    else:
        lst.removeHead()
ans = lst.head
while ans != None:
    print(ans.data.value, end=" ")
    ans = ans.next
