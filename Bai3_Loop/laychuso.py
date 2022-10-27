n = int(input())

while n > 0:
    digit = n % 10
    n //= 10
    print(digit, end=" ")
