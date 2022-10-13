def write_char_first_upper(n):
    result = ""
    upper_char = [i for i in range(65, 91)]
    lower_char = [j for j in range(97, 123)]
    len_result = 0
    char_upper = False

    for i in range(0, len(n)):
        if n[i] == ' ' and len_result > 0:
            result += n[i]
            char_upper = True

        elif i == 0 or n[i] == ' ' or char_upper == True:
            if ord(n[i]) in upper_char or n[i] == ' ':
                result += n[i]
            else:
                ch = ord(n[i])
                result += chr(ch-32)
            len_result += 1
            char_upper = False
        else:
            if ord(n[i]) in lower_char or n[i] == ' ':
                result += n[i]
            else:
                ch = ord(n[i])
                result += chr(ch+32)
            len_result += 1
    return result


a = []
k = int(input())


for j in range(k):
    value_row = input()
    a.append(value_row)

for i in a:
    print(write_char_first_upper(i))
print()
