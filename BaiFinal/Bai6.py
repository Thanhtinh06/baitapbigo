def convertPassWord(password):
    strEven = ''
    term = ''
    ans = ''
    for i in range (len(password)):
      if i % 2 != 0:
        strEven += password[i]
        term += '_'
      else:
        term += password[i]
    strEvenReverve = strEven[::-1]
    i = 0
    for item in term:
      if item == '_':
        ans += strEvenReverve[i]
        i += 1
      else:
        ans += item
    return ans
    
password = input()

print(convertPassWord(password))