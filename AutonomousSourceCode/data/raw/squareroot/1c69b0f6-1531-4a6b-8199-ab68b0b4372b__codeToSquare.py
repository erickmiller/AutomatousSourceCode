import numpy as np 
import random as r 
from scipy import misc
import matplotlib.pyplot as plt
import math
import os

def getColor(char):
	r = char
	g = char*char%256
	b = char*char*char%256
	return [r,g,b]

filename = os.getcwd() + '/codeToSquare.py'
filename = '/media/dodo/M3NT0R/Privat/Projekte/ticTacToe/tic5.py'
f1 = open(filename,'r')
content = f1.read()
f1.close()

content = list(content)
content2 = []
for element in content:
	content2.append(ord(element))
content = content2
length = len(content)

squareRoot = int(math.sqrt(length))+1
rest = squareRoot*squareRoot - length
restString = rest*' '
restArray = list(restString)
for element in restArray:
	content.append(ord(element))

height = squareRoot
width = squareRoot

image = []
for i in range(height):
	image.append([])

for i in range(height):
	for i2 in range(width):
		char = content[i2+i*width]
		image[i].append(getColor(char))

image = misc.toimage(image)
misc.imsave('test.png',image)

