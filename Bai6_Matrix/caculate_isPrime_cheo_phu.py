def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n//2 + 1):
            if n % i == 0:
                return False
        else:
            return True


def caculate_mutiple_isPrime_in_auxiliary_diagonal(a, nrows):
    mutiple = 1
    module = 1000003
    for i in range(nrows):
        var = a[i][nrows-i-1]
        if isPrime(var):
            mutiple *= var
    return mutiple % module


a = []
nrows = int(input())

for i in range(nrows):
    value_row = list(map(int, input().split()))
    a.append(value_row)

print(caculate_mutiple_isPrime_in_auxiliary_diagonal(a, nrows))
