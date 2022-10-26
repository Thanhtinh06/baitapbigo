class Grid:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value


n, m = map(int, input().split())
k = int(input())
result = []
for i in range(k):
    x, y, value = map(int, input().split())
    grid = Grid(x, y, value)
    if grid.value > 0:
        result.append(grid)

print(len(result))
for grid in result:
    print(f'{grid.x} {grid.y}')
