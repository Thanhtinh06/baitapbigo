class Student():
    def __init__(self, code, score):
        self.code = int(code)
        self.score = float(score)


def merge(l, n1, r, n2, a):
    i = j = k = 0
    while i < n1 and j < n2:
        if l[i].score > r[j].score or l[i].score == r[j].score and l[i].code < r[j].code:
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
        merge(l, n1, r, n2, a)
    return a


a = []
n, k = map(int, input().split())
for i in range(n):
    code, score = input().split()
    value = Student(code, score)
    a.append(value)

result = mergeShort(a, n)
for i in range(k):
    print(result[i].code)
