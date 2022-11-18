# def getAmountMath(lstQuestion,lstAns,nQues):
#     countQuestion = [0] * (10**6 + 5)
#     i = j = 0
#     count = 0
    
#     while i < len(lstQuestion):
#       countQuestion[lstQuestion[i]] += lstQuestion[i]
#       while j < len(lstAns):
#         countQuestion[lstAns[j]] -= lstAns[j]
#         if lstAns[j]-countQuestion[lstQuestion[i]] >= 0:
#           count += 1
#           break
#         j += 1
#       i += 1
#       j += 1
#     return nQues - count
                
  
# nQues, nAns = map(int,input().split())
# lstQuestion = list(map(int,input().split()))
# lstAns = list(map(int,input().split()))
# print(getAmountMath(lstQuestion,lstAns,nQues))


#Cachtoiuuhon
def getAmountMath(lstQuestion,lstAns,nQues,nAns):
  
  count = i = 0
  #Chay het mang ans de chon
  for j in range(nAns):
      if i >= nQues:
          break
      if lstAns[j] >= lstQuestion[i]:
          count += 1
          i += 1 
  return nQues - count
                
nQues, nAns = map(int,input().split())
lstQuestion = list(map(int,input().split()))
lstAns = list(map(int,input().split()))
print(getAmountMath(lstQuestion,lstAns,nQues,nAns))
