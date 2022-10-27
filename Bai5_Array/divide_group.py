def divide_group(n, a):

    result = [[],
              [],
              [], ]

    num_am = []

    for item in a:
        if item < 0 and len(result[0]) < 1:
            result[0].append(item)
        elif item > 0:
            result[1].append(item)
        elif item == 0:
            result[2].append(item)
        else:
            num_am.append(item)

    if len(result[1]) == 0 and len(num_am) % 2 == 0:
        for item in num_am:
            result[1].append(item)
    elif len(result[1]) == 0 and len(num_am) % 2 != 0:
        for i in range(0, len(num_am)):
            if i < 2:
                result[1].append(num_am[i])
            elif i == 2:
                result[2].append(num_am[i])
            else:
                result[0].append(num_am[i])
    else:
        for item in num_am:
            result[2].append(item)

    return result


n = int(input())
a = list(map(int, input().split()))
result = divide_group(n, a)
for item in result:
    print(len(item), end=" ")
    for var in item:
        print(var, end=" ")
    print()
