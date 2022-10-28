class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year


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

    def compareTwoDates(self, date1, date2):
        return date1.year > date2.year \
            or date1.year == date2.year and date1.month > date2.month \
            or date1.year == date2.year and date1.month == date2.month and date1.day > date2.day

    def check_date(self):
        if self.head == None:
            return None
        else:
            ans = self.head
            cur = self.head
            while cur != None:
                if self.compareTwoDates(cur.data, ans.data):
                    ans = cur
                cur = cur.next
            return ans


lst = LinkedList()
n = int(input())
for i in range(n):
    day, month, year = map(int, input().split())
    value = Date(day, month, year)
    lst.insertTail(value)

ans = lst.check_date()
print(ans.data.day, ans.data.month, ans.data.year)
