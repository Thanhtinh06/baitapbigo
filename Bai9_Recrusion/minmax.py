# khong de quy

# def minmax(array):
#     min = sum(array)
#     max = 0
#     i = 0
#     while i < 5:
#         list = array.copy()
#         list.pop(i)
#         sum_array = sum(list)
#         if sum_array > max:
#             max = sum_array
#         if sum_array < min:
#             min = sum_array
#         i += 1
#     return min, max


# array = [1, 3, 5, 7, 9]
# min, max = minmax(array)
# print(min, max)

# De quy
import sys
sys.setrecursionlimit(10**6)


def popArray(array, i=0):
    array.pop(i)


def creatArray(array, n, i=0, result=[]):
    if i > n-1:
        return result
    array_copy = array.copy()
    popArray(array_copy, i)
    creatArray(array, n, i+1)
    result.append(array_copy)
    return result


def sumArray(array):
    result = []
    for item in array:
        result.append(sum(item))
    return result


array = [1, 3, 5, 7, 9]
n = 5
a = creatArray(array, n)
result = sumArray(a)
min_array = min(result)
max_array = max(result)
print(min_array, max_array)
