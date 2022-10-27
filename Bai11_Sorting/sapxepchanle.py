import operator


def isEven(n):
    if n % 2 == 0:
        return True
    return False


def mergeAsc(l, n1, r, n2, a, n, isAsc):
    i = j = k = 0
    while i < n1 and j < n2:
        compare_operator = operator.lt
        if isAsc == False:
            compare_operator = operator.gt

        if compare_operator(l[i], r[j]):
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


def mergeShort(a, n, isAsc=True):
    if n > 1:
        n1 = n // 2
        n2 = n - n1
        l = a[:n1]
        r = a[n1:]
        mergeShort(l, n1, isAsc)
        mergeShort(r, n2, isAsc)
        mergeAsc(l, n1, r, n2, a, n, isAsc)
    return a


n = int(input())
a = list(map(int, input().split()))
even_numbers = []
odd_numbers = []
index_odd = []

for i in range(n):
    if isEven(abs(a[i])) == True:
        even_numbers.append(a[i])
    else:
        odd_numbers.append(a[i])
        index_odd.append(i)
shorted_even_numbers = mergeShort(even_numbers, len(even_numbers), isAsc=True)
shorted_odd_numbers = mergeShort(odd_numbers, len(odd_numbers), isAsc=False)

for i in range(len(index_odd)):
    shorted_even_numbers.insert(index_odd[i], shorted_odd_numbers[i])

for item in shorted_even_numbers:
    print(item, end=" ")
