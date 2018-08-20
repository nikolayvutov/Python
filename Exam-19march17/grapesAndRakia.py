area = float(input())
kgInM = float(input())
badGrape = float(input())

allGrape = area * kgInM
restGrape = allGrape - badGrape
rakia = restGrape * 45 / 100
sell = restGrape * 55 / 100

lRakia = (rakia / 7.5) * 9.80
lSell = sell * 1.5
print('%.2f' % lRakia)
print('%.2f' % lSell)