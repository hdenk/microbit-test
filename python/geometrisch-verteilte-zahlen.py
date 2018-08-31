from microbit import *
import random

zufallsZahl = 0
istTreffer = False
anzahlWuerfe = 0
anzahlVersuche = 0
verteilung = [0] * 65 # eins mehr !
            
def blinkLED(ms):
    display.set_pixel(2, 2, 5)
    sleep(ms / 2)
    display.set_pixel(2, 2, 0)
    sleep(ms / 2)
    
while True:
	# Wuerfeln bis Treffer
    while not istTreffer:
        zufallsZahl = random.randint(1, 6) 
        anzahlWuerfe = anzahlWuerfe + 1
        istTreffer = zufallsZahl == 6

    anzahlVersuche = anzahlVersuche + 1
    if anzahlVersuche % 100 == 0:
        blinkLED(50) # ein Lebenszeichen

	# Versuch in die Verteilung einpflegen
    if anzahlWuerfe < len(verteilung):
        verteilung[anzahlWuerfe] = verteilung[anzahlWuerfe] + 1
    else:
        display.scroll("w:" + str(anzahlWuerfe))

    # Ausgabe Anzahl Versuche und Verteilung 
    if anzahlVersuche % 6000 == 0:
        display.scroll("v:" + str(anzahlVersuche))
        for index in range(1, len(verteilung)):
            display.scroll(str(index) + ":" + str(verteilung[index]))

	# Reset anzahlWuerfe und istTreffer (für den naechsten Versuch) 
    anzahlWuerfe = 0
    istTreffer = False
