# Add your Python code here. E.g.
from microbit import *

def plusEins(n):
    return n + 1

def minusEins(n):
    return n - 1

def malZweiPlusX(n, x):
    return n * 2 + x

def malZweiPlusXMinusY(n, x, y):
    return n * 2 + x - y

def check():
    return malZweiPlusX(plusEins(malZweiPlusXMinusY(1, 3, 2)), 1) == 9

# hier geht's los... do we smile ? :) 
if check():
    display.show(Image.HAPPY)
else:    
    display.show(Image.SAD)


