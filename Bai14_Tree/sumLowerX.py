import sys
sys.setrecursionlimit(10**8)

class Node:
    def __init__(self,x=0, left=None, right=None) -> None:
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
        
    def sumNode(self):
      sumN = 0
      if self.left == None and self.right == None:
        return self.data
      if self.left != None:
        sumN += self.left.sumNode()
      if self.right != None:
        sumN += self.right.sumNode()
      sumN += self.data
      return sumN
          
        
class BST:
    def __init__(self) -> None:
       self.root = None
    
    def addToBST(self,x):
      if self.root == None:
        p = Node(x)
        self.root = p
      else:
        self.root.addToNode(x)
       
    def sumLowerXBST(self,valueX):
      sumLower = 0
      term = self.root
      while term != None:
        if term.data >= valueX:
          term = term.left
        elif term.data < valueX:
          root_new = term.right
          term.right = None
          sumLower += term.sumNode()
          term = root_new
      return sumLower
    
   
        
      
n,valueX = map(int,input().split())
lst = list(map(int,input().split()))
bst = BST()
for x in lst:
  bst.addToBST(x)
print(bst.sumXBST(valueX))