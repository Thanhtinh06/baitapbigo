from typing import List
import queue
import collections
# class Solution:
#     def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
#         i = 0
#         j = 0
#         while j < len(sandwiches) and students.count(sandwiches[j]) > 0:
#           if students[i] == sandwiches[j]:
#             j += 1
#             students.pop(i)
#           else:
#             student = students.pop(i)
#             students.append(student)
#         return len(students)


#cach2
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
      count = collections.Counter(students)
      n, k = len(students), 0
      while k < n and count[sandwiches[k]]:
          count[sandwiches[k]] -= 1
          k += 1
      return n - k
        
stu = [1,1,1,0,0,1]
san = [1,0,0,0,1,1]
print(Solution.countStudents(Solution,stu,san))
