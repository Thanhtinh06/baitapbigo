def getMinRotation(name):
  rotation = 0
  poiter = 'a'
  for i in range(len(name)):
    cur = name[i]
    distant = abs(ord(poiter) - ord(cur))
    if distant < 13:
      rotation += distant
    else:
      rotation += (26-distant)
    poiter = cur
    
  return rotation
      
name = input()
print(getMinRotation(name))
