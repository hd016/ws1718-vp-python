### Aufgabe - Kontaktbuch - JSON ###

import json

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

    kontaktbuch.append(kontakt)

    # Gibt nochmal das gesamte Kontaktbuch aus
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

            match = next((l for l in kontaktbuch if l['Name'] == search_value), None)
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
        print("Eintrag:", i,"|", row)
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

        if(edit_value == "Rufnummer"):
            print("Welche Rufnummer möchten Sie ändern?")
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
            print("Bitte nur Zahlen eingeben.")
            kontaktAndern()


def kontaktLoeschen():

    print("Welchen Kontakt möchten Sie löschen?")
    i = 0
    for row in kontaktbuch:
        print("Eintrag:", i,"|", row)
        i += 1
    try:
        loeschen_eingabe = int(input())

        del kontaktbuch[loeschen_eingabe]
        print("Der Kontakt wurde gelöscht.")
        menuAnzeigen()
        navigation()

    except IndexError:
        print("Bitte nur Positionen aus der Liste eingeben. Aktuell befinden sich", len(kontaktbuch),"Einträge in der Liste. Geben Sie bitte höchstens", len(kontaktbuch)-1, "ein")
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
        json.dump(kontaktbuch, outfile)

    print("Die JSON", dateiName, "wurde erfolgreich exportiert.")

    menuAnzeigen()
    navigation()


def import_json():
    print("Wie heißt die zu importierende Datei?")
    dateiName = input()

    print("Soll das Kontaktbuch erweitert werden? j/n")
    kBuchAbfrage = input()

    if kBuchAbfrage == "j":
        try:
            with open(dateiName + '.json', mode='r', encoding='utf8') as file:
                try:
                    decoded = json.load(file)

                    for line in decoded:
                        kontaktbuch.append(line)
                    print("Die JSON Datei wurde erfolgreich importiert und Ihr Kontaktbuch erweitert.")

                except (Exception):
                    print(Exception)

        except (IOError, ValueError, KeyError, TypeError):
            print("Ups, ein Fehler ist aufgetreten.")
            menuAnzeigen()
            navigation()
    else:
        try:
            with open(dateiName + '.json', 'r', encoding='utf8') as file:
                try:
                    decoded = json.load(file)

                    kontaktbuch.clear()

                    for line in decoded:
                        kontaktbuch.append(line)
                    print("Die JSON Datei wurde erfolgreich importiert und ein neues Kontaktbuch angelegt.")

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
