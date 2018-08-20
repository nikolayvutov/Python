budget = float(input())
season = input().lower()

result = 0

if budget <= 1000:
    if season == 'summer':
        result = budget * 65 / 100
    elif season == 'winter':
        result = budget * 45 / 100
elif 1000 < budget <= 3000:
    if season == 'summer':
        result = budget * 80 / 100
    elif season == 'winter':
        result = budget * 60 / 100
elif budget > 3000:
    if season == 'winter':
        result = budget * 90 / 100
    elif season == 'summer':
        result = budget * 90 / 100

if season == 'summer' and budget <= 1000:
    print('Alaska - Camp - {0:.2f}'.format(result))
elif season == 'summer' and budget <= 3000:
    print('Alaska - Hut - {0:.2f}'.format(result))
elif season == 'summer' and budget > 3000:
    print('Alaska - Hotel - {0:.2f}'.format(result))
elif season == 'winter' and budget <= 1000:
    print('Morocco - Camp - {0:.2f}'.format(result))
elif season == 'winter' and budget <= 3000:
    print('Morocco - Hut - {0:.2f}'.format(result))
elif season == 'winter' and budget > 3000:
    print('Morocco - Hotel - {0:.2f}'.format(result))