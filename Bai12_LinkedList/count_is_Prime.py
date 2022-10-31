def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n//2 + 1):
            if n % i == 0:
                return False
        else:
            return True


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

    def count_isPrime(self):
        count = 0
        if self.head == None:
            return count
        else:
            ans = self.head
            while ans != None:
                if isPrime(ans.data):
                    count += 1
                ans = ans.next
        return count


lst = LinkedList()
while True:
    x = int(input())
    if x == -1:
        break
    lst.insertTail(x)

print(lst.count_isPrime())
