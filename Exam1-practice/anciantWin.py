n =int(input())
m = float(input())
usdToBGN =float(input())

month = n * m
year = (month * 12) + (month * 2.5)
tax = year * 25 / 100
clearMoney = (year - tax) * usdToBGN
dayMoney = clearMoney / 365

print("%.2f" % dayMoney)