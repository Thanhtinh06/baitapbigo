def creat_ma_tran(nrows, ncols, a, b, p):
    list_items = [a, b]
    total_items = ncols * nrows

    for i in range(total_items):
        item = (list_items[i] + list_items[i+1]) % p
        list_items.append(item)

    a = []
    i = 0
    lenght = ncols
    while total_items > 0:
        a.append(list_items[i:lenght])
        total_items -= ncols
        i += ncols
        lenght += ncols
    return a


nrows, ncols = map(int, input().split())
a, b, p = map(int, input().split())

ma_tran = creat_ma_tran(nrows, ncols, a, b, p)

for item in ma_tran:
    for var in item:
        print(var, end=" ")
    print()
