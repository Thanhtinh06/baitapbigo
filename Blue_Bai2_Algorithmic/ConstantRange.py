# def getMaxLenght(lst,n):
#     countMax = 0
#     i = 0
#     j = 1
#     count = 0
#     if lst.count(lst[0]) == n:
#       return n
#     while i < n:
#       maxLenght = 0
#       minLenght = 0
#       while maxLenght - minLenght <= 1 and j <= n:
#         maxLenght = max(lst[i:j+1])
#         minLenght = min(lst[i:j+1])
#         count += 1
#         j += 1
#       countMax = max(countMax,count)
#       count -= 1
#       i += 1

#     return countMax
 
 
# n = int(input())
# lst = list(map(int,input().split()))
# print(getMaxLenght(lst,n))

#Cachtoiuuhon

n = int(input())
a = list(map(int, input().split()))

fre = [0] * (11)
diff = 0
j = 0
longest_range = 0

for i in range(n):
    if fre[a[i]] == 0:
        diff += 1
    fre[a[i]] += 1

    while j < n and diff > 2:
        if fre[a[j]] == 1:
            diff -= 1
        fre[a[j]] -= 1
        j += 1
    
    longest_range = max(longest_range, i - j + 1)

print(longest_range)