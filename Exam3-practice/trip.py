number = float(input())
season = input()

if number <= 100:
    print("Somewhere in Bulgaria")
    if season == 'summer':
        percent = number * 30 / 100
        print('Camp - '"%.2f" %percent)
    elif season == 'winter':
        percent = number * 70 / 100
        print('Hotel - '"%.2f"%percent)
elif number <= 1000:
    print("Somewhere in Balkans")
    if season == 'summer':
        percent = number * 40 / 100
        print('Camp - '"%.2f" % percent)
    elif season == 'winter':
        percent = number * 80 / 100
        print('Hotel - '"%.2f" %percent)
elif number > 1000:
    print("Somewhere in Europe")
    percent = number * 90 / 100
    print('Hotel - '"%.2f" % percent)
