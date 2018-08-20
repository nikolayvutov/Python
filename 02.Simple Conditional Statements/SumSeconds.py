sec1 = int(input())
sec2 = int(input())
sec3 = int(input())

sum = sec1 + sec2 + sec3

if sum < 60:
    min = 0
    sec = sum
else:
    min = sum // 60
    sec = sum % 60
if sec < 10:
    print(str(min) + ":0" + str(sec))
else:
    print(str(min) + ":" + str(sec))