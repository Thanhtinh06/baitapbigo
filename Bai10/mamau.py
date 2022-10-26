class Ribbon:
    def __init__(self, code_color, lenght, amount=1):
        self.code_color = code_color
        self.lenght = lenght
        self.amount = amount

    def update_code_color(self, ribbon):
        self.amount += 1
        self.lenght += ribbon.lenght


list_ribbons = []
n = int(input())
for i in range(n):
    code_color, lenght = map(int, input().split())
    rib = Ribbon(code_color, lenght)
    flag = True
    for ribbon in list_ribbons:
        if rib.code_color == ribbon.code_color:
            ribbon.update_code_color(rib)
            flag = False
            break
    if flag == True:
        list_ribbons.append(rib)


def sortCodeColor(ribbon):
    return ribbon.code_color


print(len(list_ribbons))
list_ribbons.sort(key=sortCodeColor)
for item in list_ribbons:
    print(item.code_color, item.lenght, item.amount)
