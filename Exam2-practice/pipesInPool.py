import math

v = int(input())
pipe1 = int(input())
pipe2 = int(input())
hours = float(input())

deb1 = pipe1 * hours
deb2 = pipe2 * hours
debit = deb1 + deb2

volume = math.floor((debit * 100) / v)
pipe1percent = math.floor((deb1 * 100) / debit)
pipe2percent = math.floor((deb2 * 100) / debit)

volumeplus = float(debit - v)
if volumeplus < v:
    print("The pool is {0}% full. Pipe 1: {1}%. Pipe 2: {2}%.".format(round(volume), round(pipe1percent), round(pipe2percent)))

if volumeplus >= v:
    print("For {0} hours the pool overflows with {1} liters.".format(hours, volumeplus))