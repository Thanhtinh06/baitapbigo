a, b = map(int, input().split())
tieu_thu = b - a
payment = 0
vat = 0.1
if(tieu_thu <= 50):
    payment = tieu_thu * 1484
elif(tieu_thu > 50 and tieu_thu <= 100):
    payment = 50 * 1484 + (tieu_thu - 50) * 1533
elif(tieu_thu > 100 and tieu_thu <= 200):
    payment = 50 * 1484 + 50 * 1533 + (tieu_thu - 100) * 1786
elif(tieu_thu > 200 and tieu_thu <= 300):
    payment = 50 * 1484 + 50 * 1533 + 100 * 1786 + (tieu_thu - 200) * 2242
elif(tieu_thu > 300 and tieu_thu <= 400):
    payment = 50 * 1484 + 50 * 1533 + 100 * \
        1786 + 100 * 2242 + (tieu_thu - 300) * 2503
elif(tieu_thu > 400):
    payment = 50 * 1484 + 50 * 1533 + 100 * 1786 + \
        100 * 2242 + 100 * 2503 + (tieu_thu - 400) * 2587

total_payment = payment + payment * vat
print(int(total_payment))
