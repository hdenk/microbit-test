from microbit import *
import random

saugerRaum = 1

schmutzInRaum1 = True

schmutzInRaum2 = True

zustand1 = Image("55100:"
               "55100:"
               "00100:"
               "00100:"
               "00100")

zustand2 = Image("55100:"
               "55100:"
               "00100:"
               "00100:"
               "55100")

zustand3 = Image("55100:"
               "55100:"
               "00100:"
               "00100:"
               "00155")

zustand4 = Image("55100:"
               "55100:"
               "00100:"
               "00100:"
               "55155")

zustand5 = Image("00155:"
               "00155:"
               "00100:"
               "00100:"
               "00100")

zustand6 = Image("00155:"
               "00155:"
               "00100:"
               "00100:"
               "55100")

zustand7 = Image("00155:"
               "00155:"
               "00100:"
               "00100:"
               "00155")

zustand8 = Image("00155:"
               "00155:"
               "00100:"
               "00100:"
               "55155")

visuellerZustand = [zustand1, zustand2, zustand3, zustand4, zustand5, zustand6, zustand7, zustand8]

def saugen():
    #Entfernt den Schmutz in dem Raum wo sich der Sauger befindet
    global schmutzInRaum1, schmutzInRaum2
    if saugerRaum == 1:
        schmutzInRaum1 = False
    elif saugerRaum == 2:
        schmutzInRaum2 = False
        
def nachRechts():
    #Bewegt den Sauger nach Rechts
    global saugerRaum
    if saugerRaum == 1:
        saugerRaum = 2

def nachLinks():
    #Bewegt den Sauger nach Links
    global saugerRaum
    if saugerRaum == 2:
        saugerRaum = 1

def zustandVisualisieren():
    #Visualisiert den Zustand der Vacuumcleaner-World
    codierterZustand = 0
    if schmutzInRaum1:
        codierterZustand += 1
    if schmutzInRaum2:
        codierterZustand += 2
    codierterZustand += (saugerRaum - 1) * 4
    display.show(visuellerZustand[codierterZustand])

def neuenSchmutzErzeugen():
    # per Zufall neuen Schmutz erzeugen
    global schmutzInRaum1, schmutzInRaum2
    if random.randint(1, 100) == 13:
        if random.randint(1, 2) == 1:
            schmutzInRaum1 = True
        else:  
            schmutzInRaum2 = True

def blinkLED(ms):
    # mittlere LED blinken lassen
    display.set_pixel(2, 2, 5)
    sleep(ms/2)    
    display.set_pixel(2, 2, 0)
    sleep(ms/2)    
    
while True: # Endlosschleife
    zustandVisualisieren()
    if button_a.is_pressed():
        nachLinks()
    if button_b.is_pressed():
        nachRechts()
    if accelerometer.current_gesture() == "shake":
        saugen()
    neuenSchmutzErzeugen()
    blinkLED(50)
