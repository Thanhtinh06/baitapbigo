def insertionShort(array):
  
    for i in range(1,len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key

array = [2,41,21,5123,5,21,4,6,]
insertionShort(array)
print ("Sorted array")
for i in range(len(array)):
    print("%d" %array[i],end=" ") 