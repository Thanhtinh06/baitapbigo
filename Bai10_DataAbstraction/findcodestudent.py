class Student:
    def __init__(self, code, math, literature):
        self.code = code
        self.math = math
        self.literature = literature


class Find:
    def find_student(self, find_code_student, student):
        result = []
        for code in find_code_student:
            for student in students:
                if code == student.code:
                    result.append([student.math, student.literature])
        return result


students = []
find_code_student = []
n, q = map(int, input().split())
for i in range(n):
    code, math, literature = map(float, input().split())
    students.append(Student(code, math, literature))
for j in range(q):
    code = int(input())
    find_code_student.append(code)

result = Find()
for item in result.find_student(find_code_student, students):
    for score in item:
        print(score, end=" ")
    print()
