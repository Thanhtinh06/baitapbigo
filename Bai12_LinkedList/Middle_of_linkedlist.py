class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head):
      pointer = head
      count_node = 0
      middle_node = 0
      while pointer != None:
        count_node += 1
        pointer = pointer.next
      middle_node = count_node // 2
      run = 0
      run_point = head
      while run_point != None:
        if run == middle_node:
          head = run_point
          head.next = run_point.next
          break
        run += 1
        run_point = run_point.next
      return head
    