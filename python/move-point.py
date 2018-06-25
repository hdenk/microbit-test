from microbit import *

def addVectors(v1, v2):
    x = v1[0] + v2[0]
    y = v1[1] + v2[1]
    return [x, y]

def constrainPoint(p):
    x = p[0]
    y = p[1]
    if x > 4:
        x = 0
    if y > 4:
        y = 0
    if x < 0:
        x = 4
    if y < 0:
        y = 4
    return [x, y]

point = [2, 2]
direction = [1, 1]

while True:
    display.clear()
    sleep(500)
    display.set_pixel(point[0], point[1], 5)
    point = constrainPoint(addVectors(point, direction))
    sleep(500)
