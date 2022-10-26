def fibonanci(n):
    if n < 2:
        return 1
    return fibonanci(n - 2) + fibonanci(n - 1)


n = int(input())
print(fibonanci(n))
