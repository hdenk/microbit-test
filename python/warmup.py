# Add your Python code here. E.g.
from microbit import *

gluecksZahl = 7

def plusEins(n):
    return n + 1

def minusEins(n):
    return n - 1

def plusGlueckszahl(n):
    global gluecksZahl
    return n + gluecksZahl

def malZweiPlusX(n, x):
    return n * 2 + x

def malZweiPlusXMinusY(n, x, y):
    return n * 2 + x - y

def check():
    return plusGlueckszahl(1) == 8

# hier geht's los... do we smile ? :) 
if check():
    display.show(Image.HAPPY)
else:    
    display.show(Image.SAD)


