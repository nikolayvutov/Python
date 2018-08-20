import math

budget = float(input())
areaHouse = float(input())
countWindows = int(input())
styrofoamInPackage = float(input())
priceStyrofoam = float(input())

restArea = areaHouse - (countWindows * 2.4)
adding = restArea + (restArea * 10 / 100)
sum = math.ceil(adding / styrofoamInPackage)
price = sum * priceStyrofoam

if budget > price:
    print('Spent: {0:.2f}\nLeft: {1:.2f}'.format(price, abs(price-budget)))
else:
    print('Need more: {0:.2f}'.format(abs(price-budget)))
