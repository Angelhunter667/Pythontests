# ELIZ Stundenrechner
# Mark Fechner, Oberfeldwebel
# ZVBw ELIZ

# Variablen
xDienst = 24.5
Anzahlx = 0
Tagdienste = 0
Tagdienststunden = 0
Wochenstundenzahl = 0
Erlaubtnorm = 41
Erlaubtgross = 48

# Eingaben
def rechner():
    print("Bitte die Anzahl x-Dienste eingeben: ")
    Anzahlx = float(input())
    if Anzahlx > 7:
        print("Falsche Eingabe, nochmal: ")
        Anzahlx = float(input())
    AnzahlxStunden = Anzahlx * 24.5
    AnzahlNachtstunden = Anzahlx * 12
    print(AnzahlxStunden, " Stunden im X Dienst.")
    print(AnzahlNachtstunden, " Stunden im Nachtdienst.")
    print("Bitte die Anzahl der Tagdienste eingeben: ")
    Tagdienste = int(input())
    
    for i in range(0, Tagdienste):
        print("Bitte Stundenzahl des Tagdienstes eingeben: ")
        Stundenzahl = float(input())
        StundenzahlGesamt = Stundenzahl + Stundenzahl
    
    print("Anzahl Gesamttagesstunden: ", StundenzahlGesamt)

    Wochenstundenzahl = AnzahlxStunden + StundenzahlGesamt
    print("Wochenstundenzahl: ", Wochenstundenzahl)
    SollStunden = Wochenstundenzahl / 3
    if SollStunden < 3:
        print("41 Wochenstunden im Soll.")
    else:
        print("48 Wochenstunden im Soll.")
        
rechner()
