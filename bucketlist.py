#### Einkaufszettel App .... ######


einkaufszettel = ['Banane','Opfel', 'Erdbeer']


print("Willkommen bei Ihrer Einkaufszettel")

def menuAnzeigen():

    print("--- \n Menü: \n - 1 Einkaufsliste anzeigen \n - 2 Einkauf hinzufügen \n - 3 Einzelne Einträge anzeigen \n - 4 Einzelne Einträge ändern \n - 5 Einkauf löschen \n - 6 Exit")
    print("Bitte geben Sie das Menü an: ")

def navi():

        while True:
            try:
                eingabe = float(input())
                break
            except ValueError:
                print("Bitte geben Sie nur ganze Zahlen ein.")

        if eingabe == 1:
            einkaufslisteAnzeigen()
        if eingabe == 2:
            einkaufHinzufugen()
        if eingabe == 3:
            einzelAnezeige()
        if eingabe == 4:
            einkaufAendern()
        if eingabe == 5:
            einkaufLoschen()
        if eingabe == 6:
            print("Das Programm wurde beendet.")
            exit()

        else:
            print("Bitte nur die angezeigten Navigationen eingeben")
            menuAnzeigen()
            navi()

def einkaufHinzufugen():

        print("Bitte geben Sie das Eintrag ein:")
        last_eintrag = input()
        einkaufszettel.append(last_eintrag)
        print("Einkaufszettel: ", last_eintrag , "wurde hinzugefügt.")
        menuAnzeigen()
        app()

def einkaufslisteAnzeigen():

        print("Die Einkaufsliste beinhaltet folgende Einkäufe:")
        if len(einkaufszettel) == 0:
            print("Einkaufsliste ist leer.")
            print("Bitte zuerst Einkauf hinzufügen.")
            einkaufHinzufugen()
        else:
            print(", ".join(einkaufszettel))
            print("----")
            menuAnzeigen()
            app()

def einzelAnezeige():

        print("Welches Eintrag möchten Sie anzeigen? (Bitte Position eingeben)")
        while True:
            try:
                einzelAnzeigeInput = int(input())
                break
            except ValueError:
                print("Bitte geben Sie nur ganze Zahlen ein.")
        try:
            print(einkaufszettel[einzelAnzeigeInput])
        except IndexError:
            print("Bitte nur Positionen aus der Liste eingeben. Aktuell befinden sich", len(einkaufszettel),"Einträge in der Liste. Geben Sie bitte höchstens", len(einkaufszettel)-1, "ein")
            einzelAnezeige()
        menuAnzeigen()
        app()

def einkaufAendern():

        einkaufszettel_index = list(enumerate(einkaufszettel))
        print(einkaufszettel_index)
        print("Welchen Eintrag möchten Sie ändern? (Bitte Position eingeben)")
        aendern_eingabe = int(input())

        if aendern_eingabe >= len(einkaufszettel) or aendern_eingabe < 0:
            print("Bitte geben Sie nur verfügbare Positionen an.")
            einkaufAendern()

        einkaufszettel[aendern_eingabe] = geaenderterEintrag()
        print("Der Eintrag wurde geändert.")
        menuAnzeigen()
        app()

def geaenderterEintrag():

        print("Bitte geben Sie den neuen Eintrag ein:")
        neuer_eintrag = input()
        return neuer_eintrag

def einkaufLoschen():

        einkaufszettel_index = list(enumerate(einkaufszettel))
        print(einkaufszettel_index)
        print("Welches Eintrag möchten Sie löschen?")

        loeschen_eingabe = int(input())
        try:
            print("Das Eintrag:",  einkaufszettel[loeschen_eingabe], "wurde gelöscht")
            einkaufszettel.remove(einkaufszettel[loeschen_eingabe])
        except IndexError:
            print("Bitte nur Positionen aus der Liste eingeben. Aktuell befinden sich", len(einkaufszettel),"Einträge in der Liste. Geben Sie bitte höchstens", len(einkaufszettel)-1, "ein")
            einkaufLoschen()

        menuAnzeigen()
        app()

def app():

    navi()

menuAnzeigen()
app()
