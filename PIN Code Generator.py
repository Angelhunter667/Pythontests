# Gehe alle PIN-Zahlen durch
for i in range(0, 10000):
# Füge je nach Zahlengröße fehlende Nullen hinzu und

    if i < 10:
        print ("000" + str(i))
    elif i < 100:
        print ("00" + str(i))
    elif i < 1000:
        print ("0" + str(i))
    else:
        print (i)
# Verlangsamung der Ausgabe (kann auch auskommentiert werden)
delay(1)
