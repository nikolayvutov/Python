def line(n):
    print('-' * 2 * n)

def body(n):
    print('-', end='')
    for i in range(n - 1):
        print('\\/', end='')
    print('-')

n = int(input())
line(n)
for i in range(n-2):
    body(n)
line(n)