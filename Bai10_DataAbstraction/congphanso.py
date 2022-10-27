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

    def sumFraction(num1, demon1, num2, demon2):
        num3 = num1 * demon2 + num2 * demon1
        demon3 = demon1 * demon2
        num3, demon3 = Fraction.reduceFraction(num3, demon3)
        return num3, demon3


num1, demon1 = map(int, input().split())
num2, demon2 = map(int, input().split())
num3, demon3 = Fraction.sumFraction(num1, demon1, num2, demon2)

print(f'{num3} {demon3}')
