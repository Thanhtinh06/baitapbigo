# insertsionSort

def insertAcs(a, n, x):
    j = n
    while j > 0:
        if a[j-1] <= x:
            break
        a[j] = a[j - 1]
        j -= 1
    a[j] = x


def insertsionSort(a, n):
    for i in range(1, n):
        x = a[i]
        insertAcs(a, i, x)
    return a


n = int(input())
a = list(map(int, input().split()))
print(insertsionSort(a, n))
