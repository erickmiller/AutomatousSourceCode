import os
import gc
import sys

from Perception import perception
from Models import ILModel


rootdir = "C:/Users/Ryan/Documents/Workspace/Raven-s-AI/Training/Objects/"

def loadObjects(root,folder):
    print "\nLoading: " + folder
    n = 0
    objects = []
    for subdir, dirs, files in os.walk(root+folder):
        for file in files:
            objects += perception(os.path.join(subdir, file),show=False)
            print str(file)+", "+str(len(objects[-1]))
            gc.collect()
    return objects

squares = loadObjects(rootdir,"Square")
triangles = loadObjects(rootdir,"Triangle")

square = ILModel()
for s in squares[0:len(squares)-5]:
    square.add(s.getData(),isCase=True)
for t in triangles[0:len(triangles)-5]:
    square.add(t.getData(),isCase=False)

print "Making Square"
square.make()

print "Checking Outputs"
print "Squares..."
for s in squares[len(squares)-5:len(squares)]:
    print square.check(s.getData())

print "Triangles..."
for t in triangles[len(triangles)-5:len(triangles)]:
    print square.check(t.getData())
