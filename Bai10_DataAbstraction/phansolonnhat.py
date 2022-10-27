class Fraction:
    def __init__(self, a=0, b=1):
        self.num = a
        self.demon = b

    def gcd(a, b):
        while b != 0:
            r = a % b
            a = b
            b = r
        return a

    def reduceFraction(num, demon):
        if num == 0:
            return 0, 1
        x = Fraction.gcd(abs(num), abs(demon))
        num = num // x
        demon = demon // x
        return num, demon


n = int(input())
num_max, demon_max = Fraction.reduceFraction(0, 1)
for i in range(n):
    num, demon = map(int, input().split())
    reduce_num, reduce_demon = Fraction.reduceFraction(num, demon)
    if num_max / demon_max < reduce_num / reduce_demon:
        num_max = reduce_num
        demon_max = reduce_demon

print(f'{num_max} {demon_max}')
