import sys
sys.setrecursionlimit(10**8)

def bubbleShort(array,n):
    if n == 1:
      return
    for i in range(n-1):
      if array[i] > array[i+1]:
        array[i], array[i+1] = array[i+1], array[i]
    bubbleShort(array,n-1)
          
  
array = [4,6,2,14,5,3,7,8]
bubbleShort(array,len(array))
for num in array:
  print(num, end=" ")