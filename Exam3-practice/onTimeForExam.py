examHours= int(input())
examMinutes = int(input())
studentHours = int(input())
studentMinutes = int(input())

dist = (examHours - studentHours) * 60 + examMinutes - studentMinutes

if dist < 0:
    print('Late')
    dist = -dist
    if dist != 0:
        if dist < 60:
            print(dist, 'minutes after the start')
        else:
            print('{0:2d}:{1:02d} hours after the start'.format(dist // 60, dist % 60))
elif dist <= 30:
    print('On time')
    if dist != 0:
        if dist < 60:
            print(dist, 'minutes before the start')
        else:
            print('{0:2d}:{1:02d} hours before the start'.format(dist // 60, dist % 60))
else:
    print('Early')
    if dist != 0:
        if dist < 60:
            print(dist, 'minutes before the start')
        else:
            print('{0:2d}:{1:02d} hours before the start'.format(dist // 60, dist % 60))