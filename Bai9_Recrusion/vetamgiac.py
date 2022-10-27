def draw_triangle(n, i=1):
    space = ' '
    symboy = '#'
    if i < n+1:
        result = space*(n-i) + symboy*i
        print(result)
        draw_triangle(n, i+1)


n = int(input())
draw_triangle(n)
