def bubbleShort(array):
    for i in range(len(array)):
      for j in range(0,len(array)-1):
        if array[j] > array[j+1]:
          array[j], array[j+1] = array[j+1], array[j]
        
  
array = [4,6,2,14,5,3,7,8]
bubbleShort(array)
for num in array:
  print(num, end=" ")