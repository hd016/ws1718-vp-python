### Aufgabe 2 - Kontaktbuch - CSV mit Dicts ####

import csv

print("--- Kontaktbuch ---")


## Kontaktbuch als Liste, die Kontakte als Dicts
global kontaktbuch
kontaktbuch = []



def menuAnzeigen():

    print("\n Menü: \n - 1 Alle Kontakte anzeigen \n - 2 Kontakt hinzufügen \n - 3 Einzelne Kontakte suchen \n - 4 Einzelne Kontakte ändern \n - 5 Kontakt löschen \n - 6 Export in eine CSV Datei (Speichern) \n - 7 Import aus einer CSV Datei (Laden) \n - 8 Programm beenden")
    print("Bitte geben Sie das Menü an: ")


def navigation():

    try:
        navigation_eingabe = int(input())

        if navigation_eingabe == 1:
            kontakteAnzeigen()

        elif navigation_eingabe == 2:
            kontaktHinzufugen()

        elif navigation_eingabe == 3:
            kontaktSuchen()

        elif navigation_eingabe == 4:
            kontaktAndern()

        elif navigation_eingabe == 5:
            kontaktLoeschen()

        elif navigation_eingabe == 6:
            export_csv()

        elif navigation_eingabe == 7:
            import_csv()

        elif navigation_eingabe == 8:
            exit()

        else:
            print("Nummer zwischen 1-8 erforderlich")
            navigation()

    except ValueError:
        print("Bitte nur Integer eingeben.")
        navigation()


def kontakteAnzeigen():
    if len(kontaktbuch) == 0:
            print("Kontaktbuch ist leer.")
            print("Bitte zuerst Kontakt hinzufügen.\n")
            print("Möchten Sie einen neuen Kontakt hinzufügen? j/n")
            eingabe = input()
            if eingabe == "j":
                kontaktHinzufugen()
            else:
                menuAnzeigen()
                navigation()
    else:
        for row in kontaktbuch:
            print(row)
        print("----")
        menuAnzeigen()
        navigation()


def kontaktHinzufugen():

    print("Anrede:")
    anrede = input()

    print("Vorname:")
    vorname_kontakt = input()

    print("Nachname:")
    nachname_kontakt = input()

    print("Staße:")
    strasse = input()

    print("Hausnummer:")
    hausnummer = input()

    print("PLZ:")
    plz = input()

    print("Stadt:")
    stadt = input()

    print("Telefon 1:")
    telefon1 = input()

    print("Telefon 2:")
    telefon2 = input()

    print("E-Mail:")
    email = input()

    kontakt = {'Anrede': anrede,'Vorname': vorname_kontakt, 'Nachname': nachname_kontakt, 'Strasse': strasse, 'Hausnummer': hausnummer, 'PLZ': plz, 'Stadt' : stadt, 'Telefon1': telefon1, 'Telefon2': telefon2, 'E-Mail': email}

    print("Kontakt", kontakt["Vorname"], ",", kontakt["Nachname"] , "wurde hinzugefügt.")

    kontaktbuch.append(kontakt)

    for row in kontaktbuch:
        print(row)

    menuAnzeigen()
    navigation()


def kontaktSuchen():

    print("\n 1 - Nach Vornamen suchen \n 2 - Nach Nachnamen suchen \n")
    try:
        navigation_eingabe = int(input())

        if navigation_eingabe == 1:
            print("Bitte geben Sie den Vornamen ein:")
            search_value = input()

            match = next((l for l in kontaktbuch if l['Vorname'] == search_value), None)
            print(match)

            afterKontaktSuchen()

        elif navigation_eingabe == 2:
            print("Bitte geben Sie den Nachnamen ein:")
            search_value = input()

            match = next((l for l in kontaktbuch if l['Nachname'] == search_value), None)
            print(match)

            afterKontaktSuchen()

        else:
            print("Bitte nur 1 - 2 eingeben")
            kontaktSuchen()

    except ValueError:
        print("Bitte nur Integer eingeben.")
        kontaktSuchen()


def afterKontaktSuchen():

    print("\n 1 - Weitere Kontakte suchen \n 2 - Zurück zur Hauptmenü")
    try:
        navigation_eingabe_unter_menu = int(input())

        if navigation_eingabe_unter_menu == 1:
            kontaktSuchen()

        elif navigation_eingabe_unter_menu == 2:
            menuAnzeigen()
            navigation()

        else:
            print("Bitte geben Sie 1 oder 2 ein.")
            afterKontaktSuchen()

    except ValueError:
        print("Bitte nur Integer eingeben.")
        afterKontaktSuchen()


def kontaktAndern():

    print("Welchen Kontakt möchten Sie ändern?")
    i = 0
    for row in kontaktbuch:
        print(i, row)
        i += 1

    print("Welchen Eintrag möchten Sie ändern? (Bitte Position eingeben)")
    aendern_eingabe = int(input())

    if aendern_eingabe >= len(kontaktbuch) or aendern_eingabe < 0:
        print("Bitte geben Sie nur verfügbare Positionen an.")
        kontaktAndern()

    else:
        print(kontaktbuch[aendern_eingabe])
        print("Welchen Eintrag möchten Sie ändern?")
        edit_value = input()

        print(kontaktbuch[aendern_eingabe][edit_value])

        print("Geben Sie den neuen Eintrag ein:")
        new_value = input()
        kontaktbuch[aendern_eingabe][edit_value] = new_value

        print(kontaktbuch[aendern_eingabe])

        print("\n 1 - Weitere Kontakte ändern \n 2 - Zurück zur Hauptmenü")

        try:
            navigation_eingabe_unter_menu = int(input())

            if navigation_eingabe_unter_menu == 1:
                kontaktAndern()

            elif navigation_eingabe_unter_menu == 2:
                menuAnzeigen()
                navigation()

            else:
                print("Bitte geben Sie 1 oder 2 ein.")
                kontaktAndern()

        except ValueError:
            print("Bitte nur Integer eingeben.")
            kontaktAndern()


def kontaktLoeschen():

    print("Welchen Kontakt möchten Sie löschen?")
    print(list(enumerate(kontaktbuch)))

    loeschen_eingabe = int(input())

    try:
        del kontaktbuch[loeschen_eingabe]
        print("Der Kontakt wurde gelöscht.")
        menuAnzeigen()
        navigation()

    except IndexError:
        print("Bitte nur Positionen aus der Liste eingeben. Aktuell befinden sich", len(kontaktbuch),"Einträge in der Liste. Geben Sie bitte höchstens", len(kontaktbuch)-1, "ein")
        kontaktLoeschen()


def export_csv():

    with open('liste.csv', 'w', newline='') as csvfile:

        fieldnames = ['Anrede', 'Vorname', 'Nachname', 'Strasse' , 'Hausnummer' , 'PLZ' , 'Stadt' , 'Telefon1' , 'Telefon2' , 'E-Mail']

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(kontaktbuch)

    print("Die CSV wurde erfolgreich exportiert.")

    menuAnzeigen()
    navigation()


def import_csv():

    with open('liste.csv') as csvfile:

        reader = csv.DictReader(csvfile,delimiter=",")

        for row in reader:
            kontaktbuch.append(row)

    print("Die CSV wurde erfolgreich importiert.")

    menuAnzeigen()
    navigation()


menuAnzeigen()
navigation()

