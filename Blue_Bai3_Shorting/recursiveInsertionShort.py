# def recursiveInsertionShort(array,i=0):
  
#     if i == len(array):
#       return
#     key = array[i]
#     j = i - 1
#     while j >= 0 and key < array[j]:
#         array[j+1] = array[j]
#         j -= 1
#     array[j+1] = key
#     recursiveInsertionShort(array,i+1)
    
#Cach2: De qui tu cuoi giam dan

def recursiveInsertionShort(array,n):
  
    if n <= 1:
      return
    recursiveInsertionShort(array,n-1)
    last = array[n-1]
    j = n - 2
    while j >= 0 and last > array[j]:
        array[j+1] = array[j]
        j -= 1
    array[j+1] = last
    

array = [2,41,21,5123,5,21,4,6,]
recursiveInsertionShort(array,len(array))
print ("Sorted array")
for i in range(len(array)):
    print("%d" %array[i],end=" ")
    
