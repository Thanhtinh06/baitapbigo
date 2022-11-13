
def getMinMaxTimeAccessPasswork(lstPass,k,correctPass):
    timeBan = 5
    lenghtCorrectPass = len(correctPass)
    timeMin = 0
    timeMax = 0
    lenghtMin = 0
    lenghtMax = 0
    lenghtLstPass = len(lstPass)
    for i in range(lenghtLstPass):
      if len(lstPass[i]) < lenghtCorrectPass:
        lenghtMin += 1
      if len(lstPass[i]) <= lenghtCorrectPass:
        lenghtMax += 1
        
    lenghtMax -= 1
    timeMin += lenghtMin + timeBan * (lenghtMin//k)
    timeMax += lenghtMax + timeBan * (lenghtMax//k)
    return timeMin + 1, timeMax + 1
   
    
lstPass = []
n, k = map(int,input().split())
for i in range(n):
  lstPass.append(input())
correctPass = input()
timeMin, timeMax = getMinMaxTimeAccessPasswork(lstPass,k,correctPass)
print(timeMin, timeMax)

