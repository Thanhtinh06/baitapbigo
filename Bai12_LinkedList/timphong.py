class Room:
    def __init__(self, code, price, isValid):
        self.code = code
        self.price = price
        self.isValid = isValid


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

    def print_isVaid(self):
        if self.head == None:
            return None
        else:
            valid = 0
            ans = self.head
            while ans != None:
                if ans.data.isValid == valid:
                    print(ans.data.code, ans.data.price)
                ans = ans.next


lst = LinkedList()
n = int(input())
for i in range(n):
    code, price, isValid = input().split()
    value = Room(code, int(price), int(isValid))
    lst.insertTail(value)

lst.print_isVaid()
