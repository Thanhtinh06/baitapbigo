def check_char_min(a):
    min_number = 1001
    array_appearant = [1001] * 100
    upper_a = a.upper()
    ans = ''
    for i in range(0, len(upper_a)-1):
        ch = ord(upper_a[i])
        if array_appearant(ord(upper_a[i])) == 1001:
            array_appearant[ch] = 0
        array_appearant[ch] += 1
    for j in range(0, len(array_appearant)-1):
        if array_appearant[j] > 0 and array_appearant < min_number:
            ans = chr(j)
            min_number = array_appearant[j]
    return ans


a = []
n = int(input())
for j in range(n):
    value_row = input()
    a.append(value_row)

for item in a:
    print(check_char_min(item))
