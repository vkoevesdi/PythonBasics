print("Prüfen Sie, ob Ihre Jahreszahl ein Schaltjahr ist.")

while True:
    try:
        jahreszahl = int(input("Geben Sie eine Jahreszahl ein: "))
        print()


    except Exception as error:
        print("Die Eingabe war ungültig.")

    else:
        break

if jahreszahl % 4 == 0 and jahreszahl % 100 != 0:
    print(jahreszahl," ist ein Schaltjahr.")

elif jahreszahl % 4 == 0 and jahreszahl % 100 == 0 and jahreszahl % 400 == 0:
    print(jahreszahl," ist ein Schaltjahr.")

else:
    print(jahreszahl," ist kein Schaltjahr.")


