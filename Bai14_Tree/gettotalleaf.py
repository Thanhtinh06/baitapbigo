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
    
    def getSumLeafNode(self):
      
      if self.left == None and self.right == None:
        return self.data
      elif self.left != None and self.right == None:
        return self.left.getSumLeafNode()
      elif self.left == None and self.right != None:
        return self.right.getSumLeafNode()
      else:
        return self.left.getSumLeafNode() + self.right.getSumLeafNode()


class BST:
    def __init__(self):
      self.root = None
    
    
    def addToBST(self,x):
      if self.root == None:
        p = Node(x)
        self.root = p
      else:
        self.root.addToNode(x)
    
    def getSumLeaf(self):
      return self.root.getSumLeafNode()
    
n = int(input())
lst = list(map(int,input().split()))
bst = BST()
for x in lst:
  bst.addToBST(x)
print(bst.getSumLeaf())