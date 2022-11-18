class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
      fre = [0] * 125
      lenghtText = len(text)
      strBalloon = 'balon'
      dictBallon = {
        'b':1,
        'a':1,
        'l':2,
        'o':2,
        'n':1
      }
      for i in range(lenghtText):
        if text[i] in strBalloon:
          fre[ord(text[i])] += 1
      minBallon = fre[ord(strBalloon[0])]
      i = 1
      while i < len(strBalloon):
        if fre[ord(strBalloon[i])] < dictBallon[strBalloon[i]] or minBallon < 1:
          return 0
        elif fre[ord(strBalloon[i])] < minBallon and minBallon > 1 and ord(strBalloon[i]) != 108 and ord(strBalloon[i]) != 111:
          minBallon = fre[ord(strBalloon[i])]
        elif fre[ord(strBalloon[i])] < minBallon * 2 and minBallon > 1 and ord(strBalloon[i]) == 108 or ord(strBalloon[i]) == 111 and fre[ord(strBalloon[i])] < minBallon * 2 and minBallon > 1:
          minBallon = fre[ord(strBalloon[i])] // 2
        i += 1
      return minBallon       


text = "krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"
print(Solution.maxNumberOfBalloons(Solution,text))