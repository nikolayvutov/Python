n = float(input())
fromValue = input()
toValue = input()

usd = 1.79549
eur = 1.95583
gbp = 2.53405

tmp = n

if fromValue == 'USD':
    tmp = n * usd
elif fromValue == 'GBP':
    tmp = n * gbp
elif fromValue == 'EUR':
    tmp = n * eur

if toValue == 'USD':
    tmp /= usd
elif toValue == 'GBP':
    tmp /= gbp
elif toValue == 'EUR':
    tmp /= eur

print('{0:.2f}'.format(tmp), toValue)