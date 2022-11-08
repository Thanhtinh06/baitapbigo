import sys
sys.setrecursionlimit(10**8)

class Node:
    def __init__(self, x=0, left=None, right=None):
        self.data = x
        self.left = left
        self.right = right
              
    def addToNode(self,x):
      
      if x < self.data:
        if self.left == None:
          p = Node(x)
          self.left = p 
        else:
          self.left.addToNode(x)
      elif x > self.data:
        if self.right == None:
          p = Node(x)
          self.right = p 
        else:
          self.right.addToNode(x)
      else:
        return
    
    def getHeightNode(self):
      
      
      if self.left == None and self.right == None:
        return 1
      
      hL = 0
      if self.left != None:
        hL += self.left.getHeightNode()
      hR = 0
      if self.right != None:
        hR += self.right.getHeightNode()
        
      return 1 + max(hL,hR)
      

      
class BST:
    def __init__(self):
      self.root = None
    
    
    def addToBST(self,x):
      if self.root == None:
        p = Node(x)
        self.root = p
      else:
        self.root.addToNode(x)
    
    def getHeightBST(self):
      return self.root.getHeightNode()
    
n = int(input())
lst = list(map(int,input().split()))
bst = BST()
for x in lst:
  bst.addToBST(x)
print(bst.getHeightBST())