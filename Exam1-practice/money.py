bitcoin = int(input())
chainesse = float(input())
comission = float(input())

bgn = bitcoin * 1168
usd = chainesse * 0.15


sum = (chainesse * 0.15) * 1.76
eur = (bgn + sum) / 1.95
tax = eur * comission / 100

answer = eur - tax
print("%.2f" % answer)