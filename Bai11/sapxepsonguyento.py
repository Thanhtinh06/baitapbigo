
def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n//2 + 1):
            if n % i == 0:
                return False
        else:
            return True


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
prime_numbers = []
non_prime_numbers = []
for i in range(n):
    if isPrime(a[i]) == True:
        prime_numbers.append([i, a[i]])
    else:
        non_prime_numbers.append(a[i])
shorted_non_prime_numbers = mergeShort(
    non_prime_numbers, len(non_prime_numbers))

for number in prime_numbers:
    shorted_non_prime_numbers.insert(number[0], number[1])

for item in shorted_non_prime_numbers:
    print(item, end=" ")
