class Apple():
    def __init__(self, weight, price):
        self.weight = weight
        self.price = price


n = int(input())
apple_best = Apple(0, 0)
index = 0
for i in range(n):
    weight, price = map(int, input().split())
    apple = Apple(weight, price)
    if apple.weight > apple_best.weight or apple.weight == apple_best.weight and apple.price > apple_best.price:
        apple_best = apple
        index = i

print(index)
