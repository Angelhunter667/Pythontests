
def addi():
    a = int(input("Bitte die erste Zahl eingeben: "))
    b = int(input("Bitte die zu addierende Zahl eingeben: "))
    c = a + b
    print(c)

def subbi():
    a = int(input("Bitte die Zahl eingeben von der subtrahiert werden soll: "))
    b = int(input("Bitte die Zahl eingeben die subtrahiert werden soll: "))
    c = a - b
    print(c)

def multipli():
    a = int(input("Bitte die erste Zahl eingeben: "))
    b = int(input("Bitte die Zahl eingeben mit der multipliziert werden soll: "))
    c = a * b
    print(c)

def dividi():
    a = int(input("Bitte die Zahl eingeben die geteilt werden soll: "))
    b = int(input("Bitte die Zahl eingeben mit der geteilt werden soll: "))
    c = a / b
    print(c)

def rechner():
    print("Hallo Michaela :-) ")
    print("Herzlich Willkommen zum Taschenrechner. Bitte wähle aus was Du rechnen lassen willst: ")
    print("Gebe addition, subtraktion, multiplikation oder dividieren ein: ")
    eingabe = input()
    if eingabe == "addition":
        addi()
    elif eingabe == "subtraktion":
        subbi()
    elif eingabe == "multiplikation":
        multipli()
    elif eingabe == "dividieren":
        dividi()
    else:
        print("Du Vollhohnk kannst ja nicht mal eine der Grundrechenarten richtig schreiben ;-P")

playAgain = "ja"
while playAgain == "ja" or playAgain == "j":
    rechner()
    print("Möchtest Du noch etwas rechnen: ja oder nein?")
    playAgain = input()
