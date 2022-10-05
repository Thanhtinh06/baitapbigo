a, b = map(int, input().split())
x = int(input())

if x % a == 0 and x % b == 0:
    print('BOTH')
elif x % a == 0 and x % b != 0:
    print('Upan')
elif x % b == 0 and x % a != 0:
    print('Ipan')
else:
    print('NO')
