def vergleicheTemperatur(temperaturen, langjaehriges_mittel):

    #durchschnitt = (temperaturen[0] + temperaturen[1] + temperaturen[2]) / 3
    #print("Die Durchschnittstemperatur beträgt: {0:.2f} °C".format(durchschnitt))
    #---
    tempStr = "Sie haben folgende Temperaturen eingegeben: "

    summe = 0

    for temp in temperaturen:
        tempStr += str(temp) + " °C, "
        summe += temp
    durchschnitt = summe / len(temperaturen)

    print(tempStr)
    #---

    print("Die Durchschnittstemperatur beträgt: {0:.2f} °C".format(durchschnitt))
    
    if durchschnitt >= langjaehriges_mittel:
        if durchschnitt > langjaehriges_mittel:
            print("Die Temperatur liegt über dem langjährigen Mittel")
        else:
            print("Die Temperatur entspricht dem langjährigen Mittel")
    else:
        print("Die Temperatur liegt unter dem langjährigen Mittel")
    
#---------Hauptprogramm
try:
    langjaehriges_mittel = 18.23

    print("Programm zur Berechnung der Durchschnittstemperatur\n")
    print("Geben Sie bitte die Temperaturwerte in °C ein!")

    eingabeWerte = list()

    while True:

        try:
            
            t = input("Temperaturwert = ")
            t = t.replace(",",".")
            temp = float(t)
            eingabeWerte.append(temp)

        except Exception as ex:
            "print(ex.args[0]"
            print("Bitte versuchen Sie es noch einmal")

        else:

            abfrage = input("Möchten Sie einen weiteren Wert eingeben? y/n:")
            if abfrage == "n":
                break


            '''
            temperatur1 = float(input("1. Wert: "))
            temperatur2 = float(input("2. Wert: "))
            temperatur3 = float(input("3. Wert: "))
            temperatur4 = float(input("4. Wert: "))
            temperatur5 = float(input("5. Wert: "))
            '''

                
            #tempList = [temperatur1, temperatur2, temperatur3,temperatur4,temperatur5]
            
            #durchschnitt = (temperatur1 + temperatur2 + temperatur3) / 3
            #print("Sie haben folgende Temperaturen eingegeben: {0} °C, {1} °C, {2} °C"
            #     .format(temperatur1, temperatur2, temperatur3))
            #print("Die Durchschnittstemperatur beträgt: {0:.2f} °C".format(durchschnitt))

            vergleicheTemperatur(eingabeWerte, langjaehriges_mittel)
            

except Exception as e:
    print("Es ist ein Fehler aufgetreten: \n" + e.args[0])
