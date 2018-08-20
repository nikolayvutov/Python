n = input().lower().split(' ')

unique = list()
count = dict()

for i in n:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
        unique.append(i)

ans = list()

for key in unique:
    if count[key] % 2 == 1:
        ans.append(key)

print(' '.join(ans))