
class Solution:
    def addBinary(self, a: str, b: str) -> str:
      lengthA = len(a)
      lengthB = len(b)
      maxLength = max(lengthA,lengthB)
      newArrA = []
      newArrB = []
      i = maxLength - 1
      if lengthA != lengthB:
        while i >= 0:
          if i > lengthA:
            newArrA.append('0')
          else: 
            newArrA.append(a[i])
          if i > lengthB:
            newArrB.append('0')
          else: 
            newArrB.append(b[i])
          i -= 1
      else:
        newArrA = list(a)
        newArrB = list(b)
       
      result = [] 
      term = '0'
      i = len(newArrA) - 1
      while i >= 0:
        value = newArrA[i] + newArrB[i] + term
        valueCheck = Solution.checkOne(Solution,value)
        if valueCheck == '0':
          result.insert(0,valueCheck)
          term = '0'
        elif valueCheck[0] == '0' and valueCheck[1] == 2:
          term = '1'
          result.insert(0,'0')
          newArrA.insert(0,'0')
          newArrB.insert(0,'0')
          i += 1
        elif valueCheck[0] == '1' and valueCheck[1] == 1:
          result.insert(0,'1')
          term = '0'
        elif valueCheck[0] == '1' and valueCheck[1] == 3:
          result.insert(0,'11')
        i -= 1
      
      
      strResult = result.join(" ")
          
      return strResult
    
    def checkOne(self,string):
      count = 0
      for char in string:
        if char == '1':
          count += 1
      if count % 2 == 0 and count > 0:
        value = ['0',count]
        return value
      elif count % 2 != 0 and count > 0:
        value = ['1',count]
        return value 
      else:
        return '0'       
      

      

      
a = "1010"
b = "1011"
print(Solution.addBinary(Solution,a,b))


        