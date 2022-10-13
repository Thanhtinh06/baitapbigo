def write_upper_after_poiter(n):
    result = ""
    upper_char = [i for i in range(65, 91)]
    space_cau = False

    for i in range(0, len(n)):
        if n[i] == ' ':
            result += n[i]
            if n[i-1] == '.':
                space_cau = True
        elif space_cau == True:
            if ord(n[i]) in upper_char:
                result += n[i]
            else:
                ch = ord(n[i])
                result += chr(ch-32)
            space_cau = False
        else:
            result += n[i]
    return result


n = input()
print(write_upper_after_poiter(n))
