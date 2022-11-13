class Node:
    def __init__(self, x,next=None):
        self.val = x
        self.next = next
        
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


def getIntersectionNode(headA, headB):
    lstNew = []
    poiterA = headA
    while poiterA != None:
      poiterB = headB
      while poiterB != None:
        if poiterA.val == poiterB.val:
          if poiterA.val not in lstNew:
            lstNew.append(poiterA.val)
        poiterB = poiterB.next
      poiterA = poiterA.next
    return lstNew

lst1 = LinkedList()
lst2 = LinkedList()
count = 0
while True:
    x = int(input())
    if x == -1:
      count += 1
    if count == 2:
      break
    if count == 0 and x != -1:
      lst1.insertTail(x)
    elif count == 1 and x != -1:
      lst2.insertTail(x)
    
headA = lst1.head
headB = lst2.head

ans = getIntersectionNode(headA,headB)

if len(ans) == 0:
  print('NO INTERSECTION')
else:
  ans.sort()
  for item in ans:
    print(item, end=" ")