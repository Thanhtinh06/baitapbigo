class Solution:
    def longestNiceSubstring(self, s: str) -> str:
      i = 0
      term = ''
      result = ''
      flag = False
      count = 0
      for j in range(1,len(s)):
        termI = [i,j]
        if s[i] == s[j] or abs(ord(s[i]) - ord(s[j])) == 32:
          term = s[termI[0]:termI[1]+1]
          if j == len(s) - 1:
            result += term
          flag = True
        elif s[i] != s[j] and abs(ord(s[i]) - ord(s[j])) != 32:
          count += 1
          i = j
          if flag == True:
            result += term
            flag = False
        if count > 1 and result != '':
          break
      return result

s = "YazaAay"
print(Solution.longestNiceSubstring(Solution,s))