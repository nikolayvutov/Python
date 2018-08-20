n = int(input())

s = set()
ans = []

for i in range(n):
    name = input()
    if name in s:
        continue
    else:
        s.add(name)
        ans.append(name)

for i in ans:
    print(i)