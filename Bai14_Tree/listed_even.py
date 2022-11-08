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
    
    def printPostorderTraversal(self):
        if self.left != None:
          self.left.printPostorderTraversal()
        
        if self.right != None:
          self.right.printPostorderTraversal()
        if self.data % 2 == 0:
          print(self.data, end=" ")
        
        
class BST:
    def __init__(self) -> None:
       self.root = None
    
    def addToBST(self,x):
      if self.root == None:
        p = Node(x)
        self.root = p
      else:
        self.root.addToNode(x)
       
    def printPostorderTraversalBST(self):
        self.root.printPostorderTraversal()




n = int(input())
lst = list(map(int,input().split()))
bst = BST()
for x in lst:
  bst.addToBST(x)
bst.printPostorderTraversalBST()