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
n = int(input())
a = list(map(int,input().split()))
for i in range(n):
  if i == 0:
    p = Node(a[i])
    lst.head = lst.tail = p
  else:
    x = a[i] + a[i-1]
    lst.insertTail(x)

ans = lst.head
while ans != None:
    print(ans.data, end=" ")
    ans = ans.next
    