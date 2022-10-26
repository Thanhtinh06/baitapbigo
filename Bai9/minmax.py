# khong de quy

def minmax(array):
    min = sum(array)
    max = 0
    i = 0
    while i < 5:
        list = array.copy()
        list.pop(i)
        sum_array = sum(list)
        if sum_array > max:
            max = sum_array
        if sum_array < min:
            min = sum_array
        i += 1
    return min, max


# array = [1, 3, 5, 7, 9]
# min, max = minmax(array)
# print(min, max)

# De quy


# def minMaxArray(array, min, max=0, i=0):

    # array = [1, 3, 5, 7, 9]
    # min = sum(array)
    # min, max = minMaxArray(array, min)
    # print(min, max)
