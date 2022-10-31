class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head):
        value_decimal = 0
        pointer = head
        count = 0
        while pointer != None:
          count += 1
          pointer = pointer.next
        power_var = count - 1
        ans = head
        while ans != None:
          value_decimal += ans.val * (2 ** power_var)
          power_var -= 1
          ans = ans.next
        return value_decimal