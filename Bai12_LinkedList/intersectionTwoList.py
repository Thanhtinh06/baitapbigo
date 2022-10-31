from typing import Optional

class ListNode:
    def __init__(self, x,next=None):
        self.val = x
        self.next = next

class Solution:
  
    def get_count(self,head):
        count = 0
        while head != None:
            count += 1
            head = head.next
        return count
  
    def update_head(self,head,skip_node):
        skip_nodeA = skip_node
        while skip_nodeA != 0:
          head = head.next
          skip_nodeA -= 1
        return head
    
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is headB:
          return headA
        
        count_A = self.get_count(headA)
        count_B = self.get_count(headB)
        skip_node = abs(count_A - count_B)
        
        if count_A > count_B:
            headA = self.update_head(headA,skip_node)
        elif count_A < count_B:
            headB = self.update_head(headB,skip_node)

        while headA != None and headB != None:
            if headA is headB:
              return headA
            headA = headA.next
            headB = headB.next
        return None
    
   
