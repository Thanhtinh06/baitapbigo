def getStringVitaly(strS):
    ans = ''
    indexCuoi = len(strS) - 1
    i = indexCuoi
    while i >= 0:
      if strS[i] != 'z' and i == indexCuoi:
        ans += chr(ord(strS[i])+1)
      elif strS[i] == 'z' and i == indexCuoi:
        ans += 'a'
        indexCuoi -= 1
      else:
        ans += strS[i]
      i -= 1
    return ans[::-1]
      
strS = input()
strT = input()
ans = getStringVitaly(strS)
if ans == strS or ans == strT:
  print("No such string")
else:
  print(ans)
