unique = []
s = {}

while True:
    n = input().split(' : ')
    if n[0] != 'Over':
        if n[1] != str(n[1]):
            n[0], n[1] = n[1], n[0]
            # is not switching
            unique.append(n)
        else:
            unique.append(n)
    else:
        break
for i in unique:
    print(i)