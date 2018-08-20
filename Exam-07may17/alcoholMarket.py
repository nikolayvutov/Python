uiskeyPrice = float(input())
quantityBeer = float(input())
quantityWine = float(input())
quantityRakia = float(input())
quantityUiskey = float(input())

rakiaPrice = uiskeyPrice / 2
winePrice = rakiaPrice - (rakiaPrice * 0.40)
beerPrice = rakiaPrice - (rakiaPrice * 0.80)

uiskey = uiskeyPrice * quantityUiskey
rakia = rakiaPrice * quantityRakia
wine = winePrice * quantityWine
beer = beerPrice * quantityBeer

sum = uiskey + rakia + wine + beer
print('%.2f' %sum)
