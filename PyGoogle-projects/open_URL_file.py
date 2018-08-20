import webbrowser
import time

tatal_breaks = 2
break_count = 0

print('This program started on' +time.ctime())
while (break_count < tatal_breaks):
    time.sleep(4)
    webbrowser.open('https://www.youtube.com/watch?v=fyaI4-5849w')
    break_count += 1
