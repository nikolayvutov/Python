import os
import shutil

#os.mkdir('./Exercises-Resource/Re-Directory/input/test')
#os.mkdir('./Exercises-Resource/Re-Directory/input/txt')
#os.mkdir('./Exercises-Resource/Re-Directory/input/png')

source = './Exercises-Resource/Re-Directory/input + s'

dest1 = './Exercises-Resource/Re-Directory/input/test + s'
dest2 = './Exercises-Resource/Re-Directory/input/txt + s'
dest3 = './Exercises-Resource/Re-Directory/input/png + s'

files = os.walk(source)

for f in files:
    if f == r'[^.?!]*(?<=.test)':
        shutil.move(f, dest1)
    elif f == r'[^.?!]*(?<=.txt)':
        shutil.move(f, dest2)
    elif f == r'[^.?!]*(?<=.png)':
        shutil.move(f, dest3)
