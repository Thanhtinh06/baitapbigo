def sortArray(a):
    term = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                term = a[i]
                a[i] = a[j]
                a[j] = term
    return a


a = [4, 5, 6, 2, 1, 0]
print(sortArray(a))
