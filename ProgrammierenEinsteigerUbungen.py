liste1 = [3,6,123,54,927]
i = 0
while i < len(liste1):
    print(liste1[i])
    i += 1
    
liste2 = [3,6,123,54,927]
for inhalt in liste2:
    print(inhalt)

dic = {"Marke":"VW","Modell":"Golf","Baujahr":"2011","Preis":5000}
for inhalt in dic:
    print(inhalt,dic[inhalt])



liste = [12,18,3,6,46,234,23]

wert = eval(input("Welcher Wert soll dividiert werden?:"))
for n in liste:
    if n == 0:
        print("Fehler: Zahlen dürfen nicht durch 0 geteilt werden.")
        continue
    print(wert/n)

# quadratliste = [1,2,3,4,5,6,7,8,9,10]
#i = 0
#while i < 11:
#    print(i*i)
#    i = i + 1

#for n in range(1,11):
#    print(n*n)
    
cities = ["Köln","Bonn","Berlin","Geilenkirchen","Dillingen","Ulm","Antwerpen","Brüssel","Düsseldorf","Gangelt"]
i = 0
print(cities)
for n in cities:
    print(n)
while i < 10:
    print(cities[i])
    i += 1

while True:
    zahl = eval(input("Welche Zahl möchten Sie verdoppeln?:"))
    print("Doppelter Wert: ", zahl*2)
    weiter = input("Möchten Sie fortfahren? (ja/nein) ")
    if weiter != "ja":
        break
    
def begruessung():
    print("Herzlich Willkommen!")

begruessung()

