### Aufgabe - Kontaktbuch - JSON ###

from tinydb import TinyDB, Query
from tinydb.operations import delete

import json

print("--- Kontaktbuch ---")

## Datenbank
global db
db = TinyDB('db.json')
kontakte = Query()

def menuAnzeigen():

    print("\n Menü: \n - 1 Alle Kontakte anzeigen \n - 2 Kontakt hinzufügen \n - 3 Einzelne Kontakte suchen \n - 4 Einzelne Kontakte ändern \n - 5 Kontakt löschen \n - 6 Export in eine JSON Datei (Speichern) \n - 7 Import aus einer JSON Datei (Laden) \n - 8 Programm beenden")
    print("Bitte geben Sie das Menü an: ")


def navigation():

    try:
        navigation_eingabe = int(input())

    except ValueError:
        print("Bitte nur Zahlen eingeben.")
        navigation()

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
        export_json()

    elif navigation_eingabe == 7:
        import_json()

    elif navigation_eingabe == 8:
        exit()

    else:
        print("Nummer zwischen 1-8 erforderlich")
        navigation()



def kontakteAnzeigen():
    if len(db) == 0:
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
        for row in db.all():
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

    # Beliebige Rufnummern hinzufügen
    print("Möchten Sie eine neue Telefonnummer hinzufügen? j/n")
    abfrage = input()
    telefon = []
    while abfrage == "j":

        telefon_type = rufnummerHinzufuegen()
        print("Wie lautet die neue Rufnummer?")
        nummer = str(input())

        telDict = {"Typ": telefon_type, "Nummer": nummer}
        telefon.append(telDict)
        print("Die Rufnummer:", nummer, "wurde als Typ:", telefon_type, "hinzugefügt.")

        print("Möchten Sie eine neue Telefonnummer hinzufügen? j/n")
        abfrage = input()

    # Beliebige E-Mail Adressen hinzufügen
    print("Möchten Sie eine neue E-Mail Adresse hinzufügen? j/n")
    abfrage = input()
    email = []
    while abfrage == "j":

        email_type = emailHinzuefuegen()
        print("Wie lautet die neue E-Mail Adresse?")
        email_adresse = str(input())

        emailDict = {"Typ": email_type, "E-Mail": nummer}
        email.append(emailDict)
        print("Die E-Mail Adresse:", email_adresse, "wurde als Typ:", email_type, "hinzugefügt.")

        print("Möchten Sie eine neue E-Mail Adresse hinzufügen? j/n")
        abfrage = input()


    kontakt = {
        'ID': str(len(db)+1),
        'Anrede': anrede,
        'Vorname': vorname_kontakt,
        'Name': nachname_kontakt,
        'Straße': strasse,
        'Hausnummer': hausnummer,
        'PLZ': plz,
        'Stadt' : stadt,
        'Rufnummer': telefon,
        'E-Mail': email}

    print("Kontakt", kontakt["Vorname"], ",", kontakt["Name"] , "wurde hinzugefügt.")

    db.insert(kontakt)

    # Gibt nochmal das gesamte Kontaktbuch aus
    for entry in db.all():
        print(entry)

    menuAnzeigen()
    navigation()


def kontaktSuchen():

    print("\n 1 - Nach Vornamen suchen \n 2 - Nach Nachnamen suchen \n")
    try:
        navigation_eingabe = int(input())

        if navigation_eingabe == 1:
            print("Bitte geben Sie den Vornamen ein:")
            search_value = input()

            for entry in db.search(kontakte['Vorname'].search(search_value)):
                print(entry)

            afterKontaktSuchen()

        elif navigation_eingabe == 2:
            print("Bitte geben Sie den Nachnamen ein:")
            search_value = input()

            for entry in db.search(kontakte['Name'].search(search_value)):
                print(entry)

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

    for row in db.all():
        print(row)

    print("Welchen Kontakt möchten Sie ändern? (Bitte ID eingeben)")
    aendern_eingabe = input()

    print("Welchen Eintrag möchten Sie ändern?")
    edit_value = input()


    if(edit_value == "Rufnummer"):
        print("Welche Rufnummer möchten Sie ändern?")

        for row in kontaktbuch[aendern_eingabe][edit_value]:
            print(row)

        inputOne = int(input())
        print(kontaktbuch[aendern_eingabe][edit_value][inputOne])
        print("Welchen Eintrag möchten Sie ändern?")
        inputTwo = input()
        print("Geben Sie den neuen Eintrag ein:")
        inputNewValue = input()
        kontaktbuch[aendern_eingabe][edit_value][inputOne][inputTwo] = inputNewValue

        print("Der Eintrag wurde geändert.")
        print(kontaktbuch[aendern_eingabe])


    elif(edit_value == "E-Mail"):
        print("Welche E-Mail Adresse möchten Sie ändern?")
        i = 0
        for row in kontaktbuch[aendern_eingabe][edit_value]:
            print("Eintrag:", i, "|", row)
            i += 1

        inputOne = int(input())
        print(kontaktbuch[aendern_eingabe][edit_value][inputOne])
        print("Welchen Eintrag möchten Sie ändern?")
        inputTwo = input()
        print("Geben Sie den neuen Eintrag ein:")
        inputNewValue = input()
        kontaktbuch[aendern_eingabe][edit_value][inputOne][inputTwo] = inputNewValue

        print("Der Eintrag wurde geändert.")
        print(kontaktbuch[aendern_eingabe])

    else:

        print("Geben Sie den neuen Eintrag ein:")
        new_value = input()

        db.update({edit_value: new_value}, kontakte['ID'].search(aendern_eingabe))


        for entry in db.search(kontakte['ID'].search(aendern_eingabe)):
            print(entry)

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
        print("Bitte nur Zahlen eingeben.")
        kontaktAndern()


def kontaktLoeschen():

    print("Welchen Kontakt möchten Sie löschen? (Bitte ID eingeben)")

    for row in db.all():
        print(row)

    try:
        loeschen_eingabe = input()

        db.remove(kontakte['ID'].search(loeschen_eingabe))
        print("Der Kontakt wurde gelöscht.")
        menuAnzeigen()
        navigation()

    except IndexError:
        print("Bitte nur Positionen aus der Liste eingeben. Aktuell befinden sich", len(db),"Einträge in der Liste. Geben Sie bitte höchstens", len(db)-1, "ein")
        kontaktLoeschen()

    except ValueError:
        print("Bitte nur Zahlen eingeben.")
        kontaktLoeschen()


def rufnummerHinzufuegen():
    print("Welcher Typ Nummer soll es sein? 'Mobil', 'Privat', 'Geschäftlich'.")
    type_input = input()
    telefon_type = ""

    if (type_input == "Mobil"):
        telefon_type = "Mobil"
    elif (type_input == "Privat"):
        telefon_type = "Privat"
    elif (type_input == "Geschäftlich"):
        telefon_type = "Geschäftlich"
    else:
        rufnummerHinzufuegen()

    return telefon_type

def emailHinzuefuegen():
    print("Welcher Typ E-Mail Adresse soll es sein? 'Privat', 'Geschäftlich'.")
    type_input = input()
    email_type = ""

    if (type_input == "Privat"):
        email_type = "Privat"
    elif (type_input == "Geschäftlich"):
        email_type = "Geschäftlich"
    else:
        emailHinzuefuegen()

    return email_type

def export_json():

    print("Wie soll die exportierte Datei heißen?")
    dateiName = input()
    with open(dateiName+'.json', 'w', encoding='utf-8') as outfile:

        contactbook = []
        for entry in db.all():
            contactbook.append(entry)

        json.dump(contactbook, outfile, indent=4)

    print("Die JSON", dateiName, "wurde erfolgreich exportiert.")

    menuAnzeigen()
    navigation()


def import_json():
    print("Wie heißt die zu importierende Datei?")
    dateiName = input()

    try:
        with open(dateiName + '.json', mode='r', encoding='utf8') as file:
            try:
                decoded = json.load(file)
                db.purge() # Datenbank wird geleert

                for line in decoded:
                    db.insert(line)
                print("Die JSON Datei wurde erfolgreich importiert und Ihr Kontaktbuch erweitert.")

            except (Exception):
                print(Exception)

    except (IOError, ValueError, KeyError, TypeError):
        print("Ups, ein Fehler ist aufgetreten.")
        menuAnzeigen()
        navigation()


    menuAnzeigen()
    navigation()


menuAnzeigen()
navigation()
