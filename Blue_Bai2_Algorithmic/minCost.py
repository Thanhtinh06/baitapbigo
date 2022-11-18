class Solution:
    def minCost(self, colors: str, neededTime) -> int:
        cost = 0
        maxValue = 0
        pre = [0,maxValue]
        for i in range(0,len(colors)):
          if ord(colors[i]) == pre[0]:
            if neededTime[i] < pre[1]:
              cost += neededTime[i]
              maxValue = pre[1]
            else:
              cost += pre[1]
              maxValue = neededTime[i]
            pre = [ord(colors[i]),maxValue]
          else:
            pre = [ord(colors[i]),neededTime[i]]
        return cost
