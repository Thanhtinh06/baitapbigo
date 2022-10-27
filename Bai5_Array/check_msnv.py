def check_msnv(n, a):
    min_msnv = min(a)
    if min_msnv > 1:
        return 1
    else:
        for i in range(n):
            if min_msnv in a:
                min_msnv += 1
                continue
            else:
                return min_msnv
        else:
            return max(a) + 1


n = int(input())
a = list(map(int, input().split()))
print(check_msnv(n, a))
