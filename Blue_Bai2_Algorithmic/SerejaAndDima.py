# def getScore(lstPoint,n):
#     scoreSereja = scoreDima = 0
#     i = 0
#     j = n -1
#     count = n
#     setPlay = 1
#     while count > 0:
#       scoreRound = 0
#       if lstPoint[i] > lstPoint[j]:
#         scoreRound = lstPoint[i]
#         i += 1
#       else:
#         scoreRound = lstPoint[j]
#         j -= 1
#       if setPlay % 2 != 0:
#         scoreSereja += scoreRound
#       else:
#         scoreDima += scoreRound
#       setPlay += 1
#       count -= 1
#     return scoreSereja, scoreDima

# n = int(input())
# lstPoint = list(map(int,input().split()))
# scoreSereja, scoreDima = getScore(lstPoint,n)
# print(scoreSereja, scoreDima)


#Refactorcode
def getScore(lstPoint,n):
    i = 0
    j = n -1
    res = [0,0]
    player = 0
    while i <= j:
      if lstPoint[i] > lstPoint[j]:
        res[player] += lstPoint[i]
        i += 1
      else:
        res[player] += lstPoint[j]
        j -= 1
      player = 1 - player
    return res

n = int(input())
lstPoint = list(map(int,input().split()))
res = getScore(lstPoint,n)
print(res[0], res[1])