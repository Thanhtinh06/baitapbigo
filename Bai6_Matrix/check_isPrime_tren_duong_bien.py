def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n//2 + 1):
            if n % i == 0:
                return False
        else:
            return True


def check_isPrime_inline(a, nrows, ncols):
    count = 0
    for i in range(0, nrows, nrows - 1):
        for j in range(ncols):
            if isPrime(a[i][j]):
                count += 1
    for j in range(0, ncols, ncols - 1):
        for i in range(1, nrows-1):
            if isPrime(a[i][j]):
                count += 1
    return count


a = []
nrows, ncols = map(int, input().split())

for i in range(nrows):
    value_row = list(map(int, input().split()))
    a.append(value_row)

print(check_isPrime_inline(a, nrows, ncols))
