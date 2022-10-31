class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
      new_node = None
      term = None
      while head != None:
        new_node = ListNode(head.val)
        head = head.next
        if term != None:
          new_node.next = term
        term = new_node
        
      return new_node
    
      
# head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,None)))))
# ans = Solution()
# r = ans.reverseList(head)
# print(r.val)
# print(r.next.next.val)