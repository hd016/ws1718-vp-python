### Aufgabe - Kontaktbuch - JSON ###

from xml.etree.ElementTree import parse
import xml.etree.ElementTree as ET

print("--- Kontaktbuch ---")


## Kontaktbuch als Liste, die Kontakte als Dicts
global kontaktbuch
kontaktbuch = []
root = parse('sample.xml').getroot()

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
        export_xml()

    elif navigation_eingabe == 7:
        import_xml()

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
        for kontakt in kontaktbuch:
            print("---------------------------------")
            all_kontakt = list(kontakt)
            for one_k in all_kontakt:
                if(one_k.attrib):
                    print(one_k.tag, one_k.attrib["Typ"], ":", one_k.text)
                else:
                    print(one_k.tag, ":", one_k.text)
        menuAnzeigen()
        navigation()


def kontaktHinzufugen():

    # Elementtree Kontakt erstellen
    kontakt = ET.Element("Kontakt")

    kAnrede = ET.SubElement(kontakt, "Anrede")
    kVorname = ET.SubElement(kontakt, "Vorname")
    kName = ET.SubElement(kontakt, "Name")
    kStrasse = ET.SubElement(kontakt, "Straße")
    kHausNr = ET.SubElement(kontakt, "Hausnummer")
    kPLZ = ET.SubElement(kontakt, "PLZ")
    kStadt = ET.SubElement(kontakt, "Stadt")

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
    while abfrage == "j":
        telefon_type = rufnummerHinzufuegen()
        print("Wie lautet die neue Rufnummer?")
        nummer = str(input())

        telDict = {"Typ": telefon_type}

        kRNummer = ET.SubElement(kontakt, "Rufnummer", telDict)
        kRNummer.text = nummer

        print("Die Rufnummer:", nummer, "wurde als Typ:", telefon_type, "hinzugefügt.")

        print("Möchten Sie eine neue Telefonnummer hinzufügen? j/n")
        abfrage = input()

    # Beliebige E-Mail Adressen hinzufügen
    print("Möchten Sie eine neue E-Mail Adresse hinzufügen? j/n")
    abfrage = input()
    while abfrage == "j":

        email_type = emailHinzuefuegen()
        print("Wie lautet die neue E-Mail Adresse?")
        email_adresse = str(input())

        emailDict = {"Typ": email_type}
        kEmail = ET.SubElement(kontakt, "Rufnummer", emailDict)
        kEmail.text = email_adresse

        print("Die E-Mail Adresse:", email_adresse, "wurde als Typ:", email_type, "hinzugefügt.")

        print("Möchten Sie eine neue E-Mail Adresse hinzufügen? j/n")
        abfrage = input()


    kAnrede.text = anrede
    kVorname.text = vorname_kontakt
    kName.text = nachname_kontakt
    kStrasse.text = strasse
    kHausNr.text = hausnummer
    kPLZ.text = plz
    kStadt.text = stadt

    root.append(kontakt)
    kontaktbuch.append(kontakt)

    # Gibt nochmal das gesamte Kontaktbuch aus
    for kontakt in kontaktbuch:
        print("---------------------------------")
        all_kontakt = list(kontakt)
        for one_k in all_kontakt:
            if (one_k.attrib):
                print(one_k.tag, one_k.attrib["Typ"], ":", one_k.text)
            else:
                print(one_k.tag, ":", one_k.text)

    menuAnzeigen()
    navigation()


def kontaktSuchen():

    print("\n 1 - Nach Vornamen suchen \n 2 - Nach Nachnamen suchen \n")
    try:
        navigation_eingabe = int(input())

        if navigation_eingabe == 1:
            print("Bitte geben Sie den Vornamen ein:")
            search_value = input()

            # Sucht nach dem gewünschten Vornamen und speichert Treffer in Variable match
            #match = [element for element in root.iter() if element.text == search_value]

            for match in root.findall(".//*[Vorname='%s']" %search_value):
                for m in match:
                    if(m.attrib):
                        print(m.tag, ":", m.attrib["Typ"], ":", m.text)
                    else:
                        print(m.tag, ":", m.text)

            # match = next((l for l in kontaktbuch if l[1] == search_value), None)
            # print(match)

            afterKontaktSuchen()

        elif navigation_eingabe == 2:
            print("Bitte geben Sie den Nachnamen ein:")
            search_value = input()

            for match in root.findall(".//*[Nachname='%s']" %search_value):
                for m in match:
                    if(m.attrib):
                        print(m.tag, ":", m.attrib["Typ"], ":", m.text)
                    else:
                        print(m.tag, ":", m.text)
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

    #ToDo: Typ noch nicht editirbar

    print("Welchen Kontakt möchten Sie ändern?")
    i = 0
    for row in kontaktbuch:
        print("Eintrag:", i,"-")
        for k in row:
            print(k.tag, k.text)
        print("---------------------------")
        i += 1

    print("Welchen Eintrag möchten Sie ändern? (Bitte Position eingeben)")
    aendern_eingabe = int(input())

    if aendern_eingabe >= len(kontaktbuch) or aendern_eingabe < 0:
        print("Bitte geben Sie nur verfügbare Positionen an.")
        kontaktAndern()

    else:
        i = -1
        for data in kontaktbuch[aendern_eingabe].iter():
            if(i == -1):
                pass
            else:
                print(i,":", data.tag, data.text)
            i += 1

        print("Welchen Eintrag möchten Sie ändern?")
        edit_value = int(input())

        print(kontaktbuch[aendern_eingabe][edit_value].tag, kontaktbuch[aendern_eingabe][edit_value].text)
        print("Geben Sie den neuen Eintrag ein:")
        new_value = input()
        kontaktbuch[aendern_eingabe][edit_value].text = new_value

        i = -1
        for data in kontaktbuch[aendern_eingabe].iter():
            if(i == -1):
                pass
            else:
                print(data.tag, data.text)
            i += 1

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
        print("Eintrag:", i,"-")
        for k in row:
            print(k.tag, k.text)
        print("---------------------------")
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

# https://norwied.wordpress.com/2013/08/27/307/
def indent(elem, level=0):
  i = "\n" + level*"  "
  if len(elem):
    if not elem.text or not elem.text.strip():
      elem.text = i + "  "
    if not elem.tail or not elem.tail.strip():
      elem.tail = i
    for elem in elem:
      indent(elem, level+1)
    if not elem.tail or not elem.tail.strip():
      elem.tail = i
  else:
    if level and (not elem.tail or not elem.tail.strip()):
      elem.tail = i

def export_xml():

    print("Wie soll die exportierte Datei heißen?")
    dateiName = input()

    indent(root)
    baum = ET.ElementTree(root)
    baum.write('%s.xml' %dateiName, xml_declaration=True, encoding='utf-8', method="xml")

    print("Die XML", dateiName, "wurde erfolgreich exportiert.")

    menuAnzeigen()
    navigation()


def import_xml():
    print("Wie heißt die zu importierende Datei? (ohne .xml angeben!)")
    dateiName = input()

    print("Soll das Kontaktbuch erweitert werden? j/n")
    kBuchAbfrage = input()

    if kBuchAbfrage == "j":
        try:
            doc = parse(dateiName+".xml")
            root = doc.getroot()

            for child in root:
                kontaktbuch.append(child)

            print("Die XML Datei wurde erfolgreich importiert und Ihr Kontaktbuch erweitert.")

        except Exception as e:
            print(str(e))
            menuAnzeigen()
            navigation()
    else:
        try:
            doc = parse(dateiName+".xml")
            root = doc.getroot()

            kontaktbuch.clear()

            for child in root:
                kontaktbuch.append(child)

            print("Die XML Datei wurde erfolgreich importiert und Ihr Kontaktbuch erstellt.")

        except Exception as e:
            print(str(e))
            menuAnzeigen()
            navigation()

    menuAnzeigen()
    navigation()


menuAnzeigen()
navigation()
