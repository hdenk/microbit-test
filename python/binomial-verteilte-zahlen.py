from microbit import *
import random

zufallsZahl = 0
istTreffer = False
anzahlTreffer = 0
anzahlWuerfe = 0
anzahlVersuche = 0
verteilung = [0] * 17
            
def blinkLED(ms):
    display.set_pixel(2, 2, 5)
    sleep(ms / 2)
    display.set_pixel(2, 2, 0)
    sleep(ms / 2)
    
while True:
	# Wuerfeln bis Treffer
    while anzahlWuerfe < len(verteilung) - 1:
        zufallsZahl = random.randint(1, 6) 
        anzahlWuerfe = anzahlWuerfe + 1
        istTreffer = zufallsZahl % 2 == 0
        if istTreffer:
            anzahlTreffer = anzahlTreffer + 1
        
    anzahlVersuche = anzahlVersuche + 1
    if anzahlVersuche % 100 == 0:
        blinkLED(50) # ein Lebenszeichen

	# Versuch in die Verteilung einpflegen
    verteilung[anzahlTreffer] = verteilung[anzahlTreffer] + 1
    #display.scroll(str(anzahlTreffer) + ":" + str(verteilung[anzahlTreffer]))

    # Ausgabe Anzahl Versuche und Verteilung 
    if button_a.is_pressed() or anzahlVersuche % 1000 == 0:
        display.scroll("v:" + str(anzahlVersuche))
        for index in range(0, len(verteilung)):
            display.scroll(str(index) + ":" + str(verteilung[index]))

	# Reset für den naechsten Versuch
    anzahlWuerfe = 0
    istTreffer = False
    anzahlTreffer = 0
