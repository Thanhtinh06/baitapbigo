def checkSortArray(arr,n):
    ascArr = sorted(arr)
    indexWrongArr = []
    for i in range(n):
      if arr[i] != ascArr[i]:
        indexWrongArr.append(i)
        
    if len(indexWrongArr) == 0:
      return True,[1,1] 
    
    arrWrong = arr[indexWrongArr[0]:indexWrongArr[-1]+1]
    arrWrong.reverse()
    
    if arrWrong == ascArr[indexWrongArr[0]:indexWrongArr[-1]+1]:
      ans = [indexWrongArr[0]+1,indexWrongArr[-1]+1]
      return True,ans 
    return False,[0,0]

n = int(input())
arr = list(map(int,input().split()))
check,index = checkSortArray(arr,n)
if check == True:
  print('yes')
else:
  print('no')
if index.count(0) != 2:     
  print(index[0],index[1])  