### Aufgabe 2 - Kontaktbuch - CSV mit dicts - ok ####

import csv

print("--- Kontaktbuch ---")


## Kontaktbuch als Liste, die Kontakte als Dicts

kontaktbuch = []


def menuAnzeigen():

    print("\n Menü: \n - 1 Kontakte anzeigen \n - 2 Kontakt hinzufügen \n - 3 Einzelne Kontakte anzeigen \n - 4 Einzelne Kontakte ändern \n - 5 Kontakt löschen \n - 6 Exit")
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
            pass

        elif navigation_eingabe == 5:
            pass

        elif navigation_eingabe == 6:
            pass

        else:
            print('not a number 1-6')
            navigation()

    except ValueError:
        print('Pls only give integer numbers.')
        navigation()


def kontakteAnzeigen():
    if len(kontaktbuch) == 0:
            print("Kontaktbuch ist leer.")
            print("Bitte zuerst Kontakt hinzufügen.")
            kontaktHinzufugen()
    else:
        print(kontaktbuch)
        print("----")


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

    global kontakt
    kontakt = {'Anrede': anrede,'Vorname': vorname_kontakt, 'Nachname': nachname_kontakt, 'Straße': strasse, 'Hausnummer': hausnummer, 'PLZ': plz, 'Stadt' : stadt, 'Telefon 1': telefon1, 'Telefon 2': telefon2, 'E-Mail': email}

    print("Kontakt", kontakt["Vorname"], ",", kontakt["Nachname"] , "wurde hinzugefügt.")

    kontaktbuch.append(kontakt)

    print(kontaktbuch)

    menuAnzeigen()
    navigation()

def kontaktSuchen():

    print("\n 1 - Nach Vornamen suchen \n 2 - Nach Nachnamen suchen \n 3 - Nach Vor- und Nachnamen suchen")
    try:
        navigation_eingabe = int(input())

        if navigation_eingabe == 1:
            print("Bitte geben Sie den Vornamen ein:")
            search_value = input()
            match = next((l for l in kontaktbuch if kontakt['Vorname'] == search_value), None)
            print(match)
            afterKontaktSuchen()

        elif navigation_eingabe == 2:
            print("Bitte geben Sie den Nachnamen ein:")
            search_value = input()
            match = next((l for l in kontaktbuch if kontakt['Nachname'] == search_value), None)
            print(match)
            afterKontaktSuchen()


        else:
            print("Bitte nur 1 - 3 eingeben")
            kontaktSuchen()

    except ValueError:
        print('Pls only give integer numbers.')
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


    menuAnzeigen()
    navigation()



menuAnzeigen()
navigation()

