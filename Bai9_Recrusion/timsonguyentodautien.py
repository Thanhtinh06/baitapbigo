# De qui


def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n//2 + 1):
            if n % i == 0:
                return False
        else:
            return True


def find_prime_first(a, index):
    if index == len(a) - 1 and isPrime(a[index]) == True:
        return index
    elif index == len(a) - 1 and isPrime(a[index]) == False:
        return -1
    else:
        if isPrime(a[index]):
            return index
    return find_prime_first(a, index+1)


n = int(input())
a = list(map(int, input().split()))
index = 0
print(find_prime_first(a, index))
