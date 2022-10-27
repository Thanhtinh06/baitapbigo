def find_digit_max(n):
    max = 0
    digit = 0
    while n > 0:
        digit = n % 10
        if digit >= max:
            max = digit
        n //= 10
    return max


n = int(input())
print(find_digit_max(n))
