import os

for file in os.listdir("./Exercises-Resource/Filter-Extensions/input"):
    if file.endswith(".txt"):
        print(os.path.join(file))