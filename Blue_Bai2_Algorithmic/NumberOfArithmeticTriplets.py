class Solution:
    def arithmeticTriplets(self, nums, diff) -> int:
      i = j = k = 0
      ans = []
      while i < len(nums):
        term = [nums[i],0,0]
        ansJ = nums[i] + diff
        ansK = nums[i] + diff * 2
        j = i
        while j < len(nums) and nums[j] <= ansJ:
          if nums[j] == ansJ:
            term[1] = nums[j]
          j += 1
        k = j
        while k < len(nums) and nums[k] <= ansK:
          if nums[k] == ansK:
            term[2] = nums[k]
          k += 1
        if term[1] != 0 and term[2] != 0:
          ans.append(term)
        i += 1
      return len(ans)
    
nums = [0,1,2]
diff = 1
print(Solution.arithmeticTriplets(Solution, nums, diff))