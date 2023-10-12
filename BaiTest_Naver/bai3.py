def findNumber(direction):
  inputArr = list(direction)
  lenghtInput = len(inputArr)
  result = {}
  answer = []
  arr = [0,2**(lenghtInput)]
  for i in range(0,lenghtInput):
    center = (arr[0] + arr[1]) // 2
    result[i+1] = center
    if inputArr[i] == 'L':
      arr = [arr[0],center]
    else:
      arr = [center,arr[1]]
  sortedResult = sorted(result.items(),key=lambda x:x[1])
  for num in sortedResult:
    answer.append(num[0])
  return answer

print(findNumber('LLLRRLLRLLRRLLLLLR'))