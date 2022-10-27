a, b, c, d = map(int, input().split())


maxcandy = a

if maxcandy < b:
    maxcandy = b
if maxcandy < c:
    maxcandy = c
if maxcandy < d:
    maxcandy = d

print(maxcandy)
