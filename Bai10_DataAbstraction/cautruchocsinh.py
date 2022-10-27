class Student:
    def __init__(self, name, score_math, score_literature):
        self.name = name
        self.score_math = score_math
        self.score_literature = score_literature

    def GPA(self):
        gpa = (float(self.score_math) + float(self.score_literature)) / 2
        return gpa


name_students = []
score_students = []
n = int(input())
for i in range(0, n*2):
    if i % 2 == 0:
        value = input()
        name_students.append(value)
    else:
        value = list(input().split())
        score_students.append(value)

for i in range(n):
    score_students[i].insert(0, name_students[i])

count = 0
for item in score_students:
    student = Student(item[0], item[1], item[2])
    if float(student.GPA()) >= 9:
        count += 1

print(count)
