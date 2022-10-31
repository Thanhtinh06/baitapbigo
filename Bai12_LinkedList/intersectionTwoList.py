from typing import Optional

class ListNode:
    def __init__(self, x,next=None):
        self.val = x
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is headB:
          return headA
        count_A = 0
        count_B = 0
        pointerA = headA
        pointerB = headB
        while pointerA != None:
            count_A += 1
            pointerA = pointerA.next
        while pointerB != None:
            count_B += 1
            pointerB = pointerB.next
        skip_node = abs(count_A - count_B)
        
        ansA = headA
        ansB = headB
        
        if count_A > count_B:
            self.update_head(ansA,skip_node)
        elif count_A < count_B:
            self.update_head(ansB,skip_node)
              
        runA = ansA
        runB = ansB
        while runA != None and runB != None:
            if runA is runB:
              return runA
            runA = runA.next
            runB = runB.next
        return None
    
    def update_head(self,head,skip_node):
        skip_nodeA = skip_node
        while skip_nodeA != 0:
          head = head.next
          skip_nodeA -= 1
