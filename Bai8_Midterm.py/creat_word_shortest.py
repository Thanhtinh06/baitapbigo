def viet_tat(n):
    result = ""
    list_n = n.split()
    for item in list_n:
        item_upper = item[0].upper()
        result += item_upper
    return result


n = input()
print(viet_tat(n))
