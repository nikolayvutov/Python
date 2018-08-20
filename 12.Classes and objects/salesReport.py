class Sale:
    def __init__(self, town, product, price, quantity):
        self.town = town
        self.product = product
        self.price = price
        self.quantity = quantity

def read_sale():
    inputData = input().split(' ')
    town = inputData[0]
    product = inputData[1]
    price = float(inputData[2])
    quantity = float(inputData[3])
    currentSale = Sale(town, product, price, quantity)
    return currentSale

towns = set()
sales = list()
numberOfSales = int(input())
for sale in range(numberOfSales):
    sale = read_sale()
    sales.append(sale)
    towns.add(sale.town)


townBySales = dict()

for currentTown in towns:
    townBySales.setdefault(currentTown, 0)
    for sale in sales:
        if sale.town == currentTown:
            townBySales[currentTown] += sale.quantity * sale.price

print(townBySales)

