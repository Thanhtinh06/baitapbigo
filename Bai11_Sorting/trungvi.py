def merge(l, n1, r, n2, a, n):
    i = j = k = 0
    while i < n1 and j < n2:
        if l[i] < r[j]:
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


n = int(input())
a = list(map(int, input().split()))
result = mergeShort(a, n)

if n % 2 == 0:
    median = (result[n//2] + result[n//2 - 1]) / 2
else:
    median = result[n//2]

print(median)
