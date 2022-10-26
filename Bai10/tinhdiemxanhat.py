import math


class FurthestDistance:
    def __init__(self, mx, my):
        self.mx = mx
        self.my = my

    def distance(nx, ny):
        distance_mn = math.sqrt((mx - nx) ** 2 + (my - ny) ** 2)
        return distance_mn

    def furthest(list_n):
        list_distance = []
        for item in list_n:
            distance_mn = FurthestDistance.distance(item[0], item[1])
            list_distance.append(distance_mn)
        max_distance = max(list_distance)
        index_maxdistance = list_distance.index(max_distance)
        return list_n[index_maxdistance]


mx, my = map(int, input().split())
n = int(input())
list_n = []
for i in range(n):
    value = list(map(int, input().split()))
    list_n.append(value)

nx, ny = FurthestDistance.furthest(list_n)
print(f'{nx} {ny}')
