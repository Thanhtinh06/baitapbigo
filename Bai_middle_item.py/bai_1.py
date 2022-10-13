def tinh_tien_taxi(so_km):

    tien_di_chuyen = 0
    discout = 0.9

    if so_km <= 1:
        tien_di_chuyen = 15000
    elif 2 <= so_km <= 5:
        tien_di_chuyen = 15000 + (so_km - 1) * 13500
    elif so_km >= 6 and so_km < 12:
        tien_di_chuyen = 15000 + 4 * 13500 + (so_km - 5) * 11000
    elif so_km >= 12:
        tien_di_chuyen = (15000 + 4 * 13500 + (so_km - 5) * 11000) * discout

    return int(tien_di_chuyen)


so_km = int(input())


print(tinh_tien_taxi(so_km))
