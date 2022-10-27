class Employee:
    def __init__(self, code, name, year_born):
        self.code = code
        self.name = name
        self.year_born = year_born


list_employee = []
n = int(input())
for i in range(n):
    code, name, year_born = input().split()
    employee = Employee(code, name, year_born)

    if len(list_employee) == 0:
        list_employee.append(employee)
    else:
        if int(employee.year_born) < int(list_employee[0].year_born):
            list_employee[0] = employee
        elif int(employee.year_born) == int(list_employee[0].year_born) and int(employee.code) <= int(list_employee[0].code):
            list_employee[0] = employee

for item in list_employee:
    print(f"{item.code} {item.name} {item.year_born}")
