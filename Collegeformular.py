# Drei Studenten: 471, 354 und 502 Punkte. Deren Ergebnisse sollen ausgegeben werden
score = 0
angaben = []
studenten_liste = []
print("Herzlich Willkommen zu unserer Auswahlseite. Bitte antworten Sie auf folgende Fragen: ")
vorname = input(str("Bitte geben Sie Ihren Vornamen ein: "))
nachname = input(str("Nun bitte den Nachnamen: "))
alter = input(str("Bitte nun Ihr Alter: "))
ergebnis = input("Als Letztes das Ergebnis Ihres letzten Tests: ")
ergebnis = int(ergebnis)
anforderung_studium = 360
anforderung_stipendium = 480
angaben.append(vorname)
angaben.append(nachname)
angaben.append(alter)
angaben = str(angaben)
if ergebnis < anforderung_studium:
    print(angaben + " wir brauchen schon Leute die Lesen und Schreiben können...")
elif ergebnis > anforderung_stipendium:
    print(angaben + " kann bei uns mit einem Stipendium studieren!")
else:
    print(angaben + " Studieren ja, Stipendium nein.")

