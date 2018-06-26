# Add your Python code here. E.g.
from microbit import *

def plusEins(n):
    return n + 1

def check():
    return plusEins(0) == 1

# hier geht's los... do we smile ? :) 
if check():
    display.show(Image.HAPPY)
else:    
    display.show(Image.SAD)


