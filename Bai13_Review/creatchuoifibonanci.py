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
     
lst = LinkedList()
node1,node2,nNode = map(int,input().split())

lst.insertTail(node1)
lst.insertTail(node2)
print(lst.head.data, lst.head.next.data, end=" ")
pointer = lst.head
for i in range(2,nNode):
    term = (pointer.data + pointer.next.data) % 1000007
    lst.insertTail(term)
    print(term, end=" ")
    pointer = pointer.next