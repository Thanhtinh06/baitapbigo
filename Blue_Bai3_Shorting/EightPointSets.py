n = 8
arrX = []
arrY = []
arrXY = []
for i in range(n):
  x,y = map(int,input().split())
  if x not in arrX:
    arrX.append(x)
  if y not in arrY:
    arrY.append(y)
  if (x,y) not in arrXY:
    arrXY.append((x,y))

if len(arrX) == len(arrY) == 3 and len(arrXY) == n:
    arrX.sort()
    arrY.sort()
    ans = (arrX[1],arrY[1])
    if ans not in arrXY:
      print('respectable')
    else:
      print('ugly')
else:
    print('ugly')