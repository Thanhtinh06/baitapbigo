from typing import List


def active_tokens(expiry_time: int, operations: List[List[int]]) -> int:
  
    typeReq = {
        'create': 0,
        'reset': 1,
    }
    activeToken = {}
    expiriedTokenId = []
    T = 0
    numberTokenActive = 0
    
    for item in operations:
      
        typeOp = item[0]
        token_id = item[1]
        timeCurrent = item[2]
        T = timeCurrent
        
        if token_id not in expiriedTokenId:
          
            if typeOp == typeReq['create'] and token_id not in activeToken.keys():
                activeToken[token_id] = timeCurrent + expiry_time
                
            if typeOp == typeReq['reset'] and token_id in activeToken.keys():
                timeExpired = activeToken[token_id]
                if timeExpired >= timeCurrent:
                    timeExpired = timeCurrent + expiry_time
                else:
                    activeToken.pop(token_id)
                    expiriedTokenId.append(token_id)
                    
    for time in activeToken:
        timeExpired = activeToken[time]
        
        if timeExpired >= T:
            numberTokenActive += 1
            
    return numberTokenActive


expiry_time = int(input())
line = int(input())
operations = []
for i in range(line):
    inputOp = list(map(int, input().split()))
    operations.append(inputOp)

print(active_tokens(expiry_time, operations))

# expiry_time = 4

# operations = [[0, 1, 1], [0, 2, 2], [1, 1, 5], [1, 2, 7]]
