from matplotlib.pyplot import flag


def check_char(n):
    result = ['B', 'I', 'G', 'O', 'b', 'i', 'g', 'o']
    flag = False
    for char in n:
        if char in result:
            flag = True

    if flag == True:
        return True
    else:
        return False


n = input()
result = check_char(n)

if result:
    print("YES")
else:
    print("NO")
