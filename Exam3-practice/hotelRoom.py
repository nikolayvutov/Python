month = input().lower()
n = int(input())

if month == 'may' or month == 'october':
    studio = 50
    ap = 65
    if n > 14:
        discount = studio * 30 / 100
        studioPrice = (studio - discount) * n
    elif n > 7:
        discount = studio * 5 / 100
        studioPrice = (studio - discount) * n

elif month == 'june' or month == 'september':
    studio = 75.20
    ap = 68.70
    if n > 14:
        discount = studio * 20 / 100
        studioPrice = (studio - discount) * n
    elif n <= 14:
        studioPrice = studio * n

elif month == 'july' or month == 'august':
    studioPrice = 76 * n
    ap = 77

if n > 14:
    aptDiscount = ap * 10 / 100
    aptPrice = (ap - aptDiscount) * n

else:
    aptPrice = ap * n

print('Apartment: {0:.2f} lv.'.format(aptPrice))
print('Studio: {0:.2f} lv.'.format(studioPrice))