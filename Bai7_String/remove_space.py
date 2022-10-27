from numpy import spacing


def remove_space(n):
    new_string = ""
    need_space = False
    space = " "
    len_new_string = 0
    for char in n:
        if char == space:
            if len_new_string > 0:
                need_space = True
        else:

            if need_space == True:
                new_string += space
                need_space = False

            new_string += char
            len_new_string += 1
    return new_string


n = input()
print(remove_space(n))
