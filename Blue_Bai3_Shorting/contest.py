# def getRank(arr,n):
#   arrCopy = arr.copy()
#   arrCopy.sort(reverse=True)
#   dictArr = {arrCopy[0]:1}
#   pre = arrCopy[0]
#   count = 2
#   for i in range(1,n):
#     if arrCopy[i] != pre:
#       dictArr[arrCopy[i]] = count
#     pre = arrCopy[i]
#     count += 1
#   ans = []
#   for i in range(n):
#     ans.append(dictArr[arr[i]])
#   return ans

#Cach2

def getRank(arr,n):
  sortedArray = sorted(arr,reverse=True)
  ranked = [0] * 2005
  for i in range(n):
    ranking = sortedArray[i]
    if not ranked[ranking]:
      ranked[ranking] = i + 1    
  return ranked

n = int(input())
arr = list(map(int,input().split()))
ranked = getRank(arr,n)
for rating in arr:
  print(ranked[rating], end=" ")
      