# Cach1
def findFirstRepeatCharacter(lst):
    result = []
    charDuplicate = []
    lenght = len(lst)
    for i in range(lenght):
        for j in range(lenght):
            if i != j and ord(lst[i]) == ord(lst[j]) and lst[i] not in charDuplicate:
                result.append([abs(i-j), lst[i], i, j])
                charDuplicate.append(lst[i])

    ans = [1001] * 4
    
    for item in result:

        if item[0] < ans[0] and item[2] < ans[3] and item[3] < ans[3]:
            ans = item
            
    return ans[1]

lst = input()
ans = findFirstRepeatCharacter(lst)
if ans == None:
    print('null')
else:
    print(ans)
