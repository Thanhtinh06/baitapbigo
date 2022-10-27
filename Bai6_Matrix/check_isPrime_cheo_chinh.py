def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n//2 + 1):
            if n % i == 0:
                return False
        else:
            return True


def check_isPrime_in_cheo(a, nrows):
    count = 0
    for i in range(nrows):
        if isPrime(a[i][i]):
            count += 1
    return count


a = []
nrows = int(input())

for i in range(nrows):
    value_row = list(map(int, input().split()))
    a.append(value_row)

print(check_isPrime_in_cheo(a, nrows))
