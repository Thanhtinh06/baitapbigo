def is_contestant_next_round(n, k, a):
    count = k
    value_min = a[k-1]
    if value_min != 0:
        for i in range(k, n):
            if a[i] >= value_min:
                count += 1
        return count
    else:
        count = a.index(0)

    return count


n, k = map(int, (input()).split())
a = list(map(int, input().split()))
print(is_contestant_next_round(n, k, a))
