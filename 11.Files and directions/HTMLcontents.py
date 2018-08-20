import os
import fileinput


inputs = [i for i in input().split(' ')]

outputFile = open('./Exercises-Resource/input.html', 'w+')
outputFile.write('<!DOCTYPE>\n<html>\n<head>')
outputFile.write('\n\t<title> </title>')
outputFile.write('\n</head>\n<body>')


while inputs[0] != 'exit':
    if inputs[0] == 'title':
        outputFile.write('\n\t<title>{}</title>'.format(inputs[1]))

    elif inputs[0][0] == 'h':
        outputFile.write('\n\t<h{}>{}</h{}>'.format(inputs[0][1], inputs[1],inputs[0][1]))
    elif inputs[0] == 'p':
        outputFile.write('\n\t<p>{}</p>'.format(inputs[1]))
    elif inputs[0] == 'div':
        outputFile.write('\n\t<div>{}</div>'.format(inputs[1]))

    inputs = [i for i in input().split(' ')]
outputFile.write('\n</body>\n</html>')

outputFile.close()
