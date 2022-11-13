def getMinus(lstHotPart,amountPart):
  timeMax = 90
  timeWatch = 0
  timeTurnOff = 15
  timeToContinuos = 15
  for part in lstHotPart:
    if part <= timeToContinuos and part < timeMax:
      timeToContinuos = part + timeTurnOff
      timeWatch = part
  timeWatch += timeTurnOff
  if timeWatch >= timeMax:
    return timeMax
  return timeWatch 
  
amountPart = int(input())
lstHotPart = list(map(int,(input().split())))
print(getMinus(lstHotPart,amountPart))