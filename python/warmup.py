# Add your Python code here. E.g.
from microbit import *

point = [2, 2]
direction = [1, 1]

def addVectors(v1, v2):
    x = v1[0] + v2[0]
    y = v1[1] + v2[1]
    return [x, y]

def check():
    return addVectors(point, direction) == [3, 3]

# hier geht's los... do we smile ? :) 
if check():
    display.show(Image.HAPPY)
else:    
    display.show(Image.SAD)


