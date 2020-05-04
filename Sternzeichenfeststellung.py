# Vorgestellter Ablauf:
# Eingabe von Datum eingeteilt in Tag und Monat
# Ausgabe des jeweiligen Sternzeichens anhand Zuordnung durch das Tool

def herausfinden():
    if month == 1 and day < 20 or month == 12 and day > 22:
        print("Steinbock")
    elif month == 2 and day > 19 or month == 1 and day > 20:
        print("Wassermann")
    elif month == 2 and day > 20 or month == 3 and day < 20:
        print("Fische")
    elif month == 3 and day > 21 or month == 4 and day < 20:
        print("Widder")
    elif month == 4 and day > 21 or month == 5 and day < 21:
        print("Stier")
    elif month == 5 and day > 22 or month == 6 and day < 21:
        print("Zwillinge")
    elif month == 6 and day > 22 or month == 7 and day < 22:
        print("Krebs")
    elif month == 7 and day > 23 or month == 8 and day < 23:
        print("Löwe")
    elif month == 8 and day > 24 or month == 9 and day < 23:
        print("Jungfrau")
    elif month == 9 and day > 24 or month == 10 and day < 23:
        print("Waage")
    elif month == 10 and day > 24 or month == 11 and day < 22:
        print("Skorpion")
    elif month == 11 and day > 23 or month == 12 and day < 21:
        print("Schütze")
 
months = {1 : "Januar", 2 : "Februar", 3 : "März", 4 : "April", 5 : "Mai", 6 : "Juni", 7 : "Juli", 8 : "August", 9 : "September", 10 : "Oktober", 11 : "November", 12 : "Dezember"}
print("Lass uns Dein Sternzeichen gemeinsam herausfinden!")
month = int(input("Bitte gib Deinen Geburtsmonat in Ziffern ein (Also 1 für Januar usw.)"))
day = int(input("Bitte gib nun Deinen Geburtstag ein: "))
print("Dein Gebutstag ist also der: ")
print(str(day) + ".")
print(months[month])
print("Dein Sternzeichen ist demnach: ")

herausfinden()