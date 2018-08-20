season = input().lower()
groupKind = input().lower()
students = int(input())
nights = int(input())

sport = 'sport'
nightPrice = 0
if groupKind == 'boys' and season == 'winter':
    sport == 'Judo'



if season == 'winter':
    if groupKind == 'boys':
        nightPrice = nights * 9.60
        sport = 'Judo'
    elif groupKind == 'girls':
        nightPrice = nights * 9.60
        sport = 'Gymnastics'
    elif groupKind == 'mixed':
        nightPrice = nights * 10
        sport = 'Ski'
elif season == 'spring':
    if groupKind == 'boys':
        nightPrice = nights * 7.20
        sport = 'Tennis'
    elif groupKind == 'girls':
        nightPrice = nights * 7.20
        sport = 'Athletics'
    elif groupKind == 'mixed':
        nightPrice = nights * 9.50
        sport = 'Cycling'
elif season == 'summer':
    if groupKind == 'boys':
        nightPrice = nights * 15
        sport = 'Football'
    elif groupKind == 'girls':
        nightPrice = nights * 15
        sport = 'Volleyball'
    elif groupKind == 'mixed':
        nightPrice = nights * 20
        sport = 'Swimming'

discount = 0
sum = students * nightPrice

if students >= 50:
    discount = sum / 2
elif 20 <= students < 50:
    discount = sum * 0.15
elif 10 <= students < 20:
    discount = sum * 0.05

allSum = sum - discount
print('{0} {1:.2f} lv.'.format(sport, allSum))