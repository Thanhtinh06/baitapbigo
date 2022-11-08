def checkSuffixStructures(strInput,strResult):
    lenghtStrInput = len(strInput)
    lenghtStrResult = len(strResult)
    flagArray = False
    newStrInput = ''
    lstCountCharResult = [0]*125
    lstCountCharInput = [0]*125
    lstCountCharNewStr = [0]*125
    for char in strResult:
        lstCountCharResult[ord(char)] += 1
    for char in strInput:
      if char in strResult:
        flagArray = True
        lstCountCharInput[ord(char)] += 1
        
    if lenghtStrInput == lenghtStrResult:
      if flagArray == True and lstCountCharResult == lstCountCharInput:
        return "array"
      else:
        return "need tree"
    elif lenghtStrInput < lenghtStrResult:
      return "need tree"
    else:
      for j in range(lenghtStrInput):
        if strInput[j] in strResult:
          newStrInput += strInput[j]
          
      resultAutomaton = ''
      indexStrResult = 0
      flagBoth = False
      flagcountBoth = True
      for i in range (len(newStrInput)):
        if newStrInput[i] == strResult[indexStrResult] and indexStrResult < lenghtStrResult:
          resultAutomaton += newStrInput[i]
          indexStrResult += 1
          if indexStrResult == lenghtStrResult and resultAutomaton == strResult:
            return "automaton"
        elif newStrInput[i] in strResult:
          flagBoth = True
        lstCountCharNewStr[ord(newStrInput[i])] += 1
      for j in range(len(lstCountCharNewStr)):
        if lstCountCharNewStr[j] < lstCountCharResult[j]:
          flagcountBoth = False
          if flagBoth == True and flagcountBoth == False:
            return "need tree"
      if  flagBoth == True and flagcountBoth == True:
        return "both"
      else:
        return "need tree"
        
          
strInput = input()
strResult = input()
print(checkSuffixStructures(strInput,strResult))

      