n = int(input())

print('*' * (2*n+1))
print('.' + '*' + ' ' * (2*n - 3) + '*' + '.')

for i in range(1, n-1):
    print('.' + '.' * i + '*' + '@' * ((2*n-3) -2*i) + '*' + '.' * i + '.')
print('.' * n +'*' + '.' * n)

for i in range(1, n-1):
    print('.' * ((n)-i) + '*' + ' ' * (i-1) + '@' + ' ' * (i-1) + '*' + '.' * ((n)-i))
print('.' + '*' + '@' * (2*n-3) + '*' + '.')
print('*' * (2*n+1))