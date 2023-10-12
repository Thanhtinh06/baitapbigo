from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        
        output = [""]
        
        for digit in digits:
            new_output = []
            for letter in phone[digit]:
                for combination in output:
                    new_output.append(combination + letter)
            output = new_output
        
        return output
      
print(Solution.letterCombinations(Solution,"23"))
      
#cach 2
        
