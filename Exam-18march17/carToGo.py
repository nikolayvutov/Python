bugdet = float(input())
season = input().lower()

sum = 0
if bugdet <= 100:
    print('Economy class')
    if season == 'summer':
        sum = bugdet * 35 / 100
    elif season == 'winter':
        sum = bugdet * 65 / 100
elif 100 < bugdet <= 500:
    print('Compact class')
    if season == 'summer':
        sum = bugdet * 45 / 100
    elif season == 'winter':
        sum = bugdet * 80 / 100
elif bugdet > 500:
    print('Luxury class')
    if season == 'summer':
        sum = bugdet * 90 / 100
    elif season == 'winter':
        sum = bugdet * 90 / 100

if bugdet > 500:
    print('Jeep - {0:.2f}'.format(sum))
elif season == 'summer':
    print('Cabrio - {0:.2f}'.format(sum))
elif season == 'winter':
    print('Jeep - {0:.2f}'.format(sum))
