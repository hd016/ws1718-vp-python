### Aufgabe 2 - Kontaktbuch - CSV mit Dicts ####

import csv
from tinydb import TinyDB, Query

db = TinyDB( 'db.json' )

kontaktListe = Query()

db_len = db.__len__()

print("--- Kontaktbuch mit DB usw was los???? OK . ---")

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

    if db_len == 0:
        print("Ihre Datenbank ist leer. Bitte fügen Sie zuerst Kontakte hinzu. Danke vielmal")
        kontaktHinzufugen()
    else:
        for kontakte in db.all():
            print(kontakte)

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

    db.insert(kontakt)

    menuAnzeigen()
    navigation()


def kontaktSuchen():

    print("\n 1 - Nach Vornamen suchen \n 2 - Nach Nachnamen suchen \n")
    try:
        navigation_eingabe = int(input())

        if navigation_eingabe == 1:
            print("Bitte geben Sie den Vornamen ein:")
            search_value_vorname = input()

            for kontakt in db.search(kontaktListe['Vorname'].search(search_value_vorname)):
                print(kontakt)

            afterKontaktSuchen()

        elif navigation_eingabe == 2:
            print("Bitte geben Sie den Nachnamen ein:")
            search_value_nachname = input()

            for kontakt in db.search(kontaktListe['Nachname'].search(search_value_nachname)):
                print(kontakt)

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
    for kontakte in db.all():
        print(db.get(doc_id = len(kontakte)), kontakte)


    print("Welchen Eintrag möchten Sie ändern? (Bitte Position eingeben)")
    aendern_eingabe = int(input())

    if aendern_eingabe >= db_len or aendern_eingabe < 0:
        print("Bitte geben Sie nur verfügbare Positionen an.")
        kontaktAndern()

    else:
        pk = db.get(doc_id = aendern_eingabe)
        print(pk)
        print("Welchen Eintrag möchten Sie ändern?")

        edit_value = input()

        #db.update({ 'Tags' : "Python" },

        print("Geben Sie den neuen Eintrag ein:")

        new_value = input()
        db.update({edit_value:new_value}, kontaktListe["doc_id"].search(pk))


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

