import math


class Point2D():
    def __init__(self, x=0, y=0):
        '''
        x,y -> location of point
        '''
        self.x = x
        self.y = y


class Triangle:
    def __init__(self, a, b, c):
        '''
        a,b,c -> instance of Fraction has attribute x,y
        '''
        self.a = a
        self.b = b
        self.c = c

    def side_length(self):
        lenght_ab = math.sqrt((self.b.x - self.a.x) **
                              2 + (self.b.y - self.a.y) ** 2)
        lenght_bc = math.sqrt((self.c.x - self.b.x) **
                              2 + (self.c.y - self.b.y) ** 2)
        lenght_ca = math.sqrt((self.c.x - self.a.x) **
                              2 + (self.c.y - self.a.y) ** 2)
        return lenght_ab, lenght_bc, lenght_ca

    def half_perimeter(self):
        lenght_ab, lenght_bc, lenght_ca = self.side_length()
        p = lenght_ab + lenght_bc + lenght_ca
        s = p / 2
        return s

    def area(self):
        lenght_ab, lenght_bc, lenght_ca = self.side_length()
        s = self.half_perimeter()
        area = math.sqrt(s * (s - lenght_ab) *
                         (s - lenght_bc) * (s - lenght_ca))
        return area


n = int(input())
sum = 0
a = []
for i in range(n):
    list = []
    for j in range(3):
        x, y = map(int, input().split())
        location = Point2D(x, y)
        list.append(location)
    triangle = Triangle(list[0], list[1], list[2])
    sum += triangle.area()

print("{0:.2f}".format(sum))
