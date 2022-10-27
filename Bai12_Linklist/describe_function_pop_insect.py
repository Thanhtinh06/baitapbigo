# def insert_element(a, k, value):
#     c = [0]
#     b = a.copy() + c
#     i = 0
#     j = 0
#     if k >= 0 and k <= len(a):
#         while j < len(a):
#             if i == k:
#                 b[i] = value
#                 j -= 1
#             else:
#                 b[i] = a[j]
#             i += 1
#             j += 1
#     return b


# a = [1, 4, 3, 25, 5, 7]
# print(insert_element(a, 2, 6))


# def remove_element(a, k):
#     b = [0] * (len(a) - 1)
#     i = 0
#     j = 0
#     if k >= 0 and k <= len(a) - 1:
#         while i < len(a):
#             if i != k:
#                 b[j] = a[i]
#             else:
#                 i += 1
#                 b[j] = a[i]
#             i += 1
#             j += 1
#         return b


# a = [1, 4, 3, 25, 5, 7]
# print(remove_element(a, 0))
