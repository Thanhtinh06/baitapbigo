import sys
sys.setrecursionlimit(10**8)

class Student:
    def __init__(self, code, name, score):
        self.code = code
        self.name = name
        self.score = score


class Node:
    def __init__(self,x=0, left=None, right=None) -> None:
        self.data = x
        self.left = left
        self.right = right
    
    def addToNode(self,x):
        if x.score < self.data.score:
          if self.left == None:
            p = Node(x)
            self.left = p
          else:
            self.left.addToNode(x)
        elif x.score > self.data.score:
          if self.right == None:
            p = Node(x)
            self.right = p 
          else:
            self.right.addToNode(x)
        else:
          return
    
    def findStudentNode(self):
        if self.right == None:
          return self.data
        else:
          return self.right.findStudentNode()
        
        
class BST:
    def __init__(self) -> None:
       self.root = None
    
    def addToBST(self,x):
      if self.root == None:
        p = Node(x)
        self.root = p
      else:
        self.root.addToNode(x)
       
    def findStudentBST(self):
        return self.root.findStudentNode()



bst = BST()
n = int(input())
for i in range(n):
  code, name, score = input().split()
  student = Student(code,name,float(score))
  bst.addToBST(student)
  
ans = bst.findStudentBST()
print(ans.code, ans.name, ans.score, end=" ")
  