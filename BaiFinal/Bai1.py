import sys
sys.setrecursionlimit(10**8)

def merge(l, n1, r, n2, a, n):
    i = j = k = 0
    while i < n1 and j < n2:
        if l[i] > r[j]:
            a[k] = l[i]
            i += 1
        else:
            a[k] = r[j]
            j += 1
        k += 1
    while i < n1:
        a[k] = l[i]
        i += 1
        k += 1

    while j < n2:
        a[k] = r[j]
        j += 1
        k += 1


def mergeShort(a, n):
    if n > 1:
        n1 = n // 2
        n2 = n - n1
        l = a[:n1]
        r = a[n1:]
        mergeShort(l, n1)
        mergeShort(r, n2)
        merge(l, n1, r, n2, a, n)
    return a


m,n,k = input().split()
lstA = list(map(int,input().split()))
lstB = list(map(int,input().split()))
lstC = lstA + lstB
lenght = len(lstC)
ans = mergeShort(lstC,lenght)
print(ans[-int(k)-1])