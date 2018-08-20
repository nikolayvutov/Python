kgVegetable = float(input())
kgFruit = float(input())
sumVegetable = int(input())
sumFruit = int(input())

priceVegetable = kgVegetable * sumVegetable
priceFruit = kgFruit * sumFruit
bgl = priceVegetable + priceFruit
eur = bgl / 1.94

print(priceVegetable)
print(priceFruit)
print(eur)