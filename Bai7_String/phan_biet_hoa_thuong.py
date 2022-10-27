def check_count_diffent_char(a):
    result = ''
    for i in range(0, len(a)):
        if result.find(a[i]) == -1:
            result += a[i]

    return len(result)


a = input()

result = check_count_diffent_char(a)

print(result)
