def seletionShort(array):

  for i in range(len(array)):
      minIndex = i
      for j in range(i+1,len(array)):
        if array[minIndex] > array[j]:
          minIndex = j
      array[i], array[minIndex] = array[minIndex], array[i]
  
array = [2,41,21,5123,5,21,4,6,]
seletionShort(array)
print ("Sorted array")
for i in range(len(array)):
    print("%d" %array[i],end=" ")