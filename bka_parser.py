#Aufgabe 1 einlesen
#####################
import sys          #
print(sys.version)  #
print("")           #
#####################

print("------ Bitte Python Version 3.5.x verwenden! Ab Version 3.5.x werden geschriebene Dictionaries aus writedict als ordered dict gespeichert! ----")
print("")

#####################################
# Module #                          #
                                    #
import csv                          #
import chardet                      #
from collections import defaultdict #
#####################################


faelle = []

global row
row = {}

def encoder():

    with open('/Users/DHarun/PycharmProjects/Vertiefung-Programmierung/Abgabe1/tb01_FaelleGrundtabelleKreise_csv.csv', 'rb') as f:
        global result
        result = chardet.detect(f.read())
        print(result)

def import_csv():

    with open('/Users/DHarun/PycharmProjects/Vertiefung-Programmierung/Abgabe1/tb01_FaelleGrundtabelleKreise_csv.csv', encoding='ISO-8859-1') as csvfile:

        next(csvfile)

        faelle = [{k: v for k, v in row.items()}


        for row in csv.DictReader(csvfile, delimiter=";")]

        global cleaned_list
        cleaned_list = [line for line in faelle if not line["Kreisart"].isdigit() and not "Straftaten insgesamt" in line["Straftat"]]


    print("Die CSV wurde erfolgreich importiert.")

    #filter()


def filter():

    filtered_list = [row for row in cleaned_list if "LK" in row["Kreisart"] and float(row["Aufklaerungsquote"]) < 50 and not "Straftaten insgesamt" in row["Straftat"]]

    with open('aufgabe1-1.csv', "w", newline='', encoding='ISO-8859-1') as filter_output:

        fieldnames = ["Stadt-/Landkreis","Straftat","Aufklaerungsquote"]

        writer = csv.DictWriter(filter_output, fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()

        for line in filtered_list:
            writer.writerow(line)

    print("Aufgabe 1-1.csv wurde exportiert.")


def bundesweite_berechnung():

    berechnen_list = [row for row in cleaned_list if row["erfasste Faelle"].isdigit() and not "Straftaten insgesamt" in row["Straftat"]]

    result = defaultdict(int)

    for d in berechnen_list:
        result[d['Straftat']] += int(d['erfasste Faelle'])

    global bundesweite_liste
    bundesweite_liste = [{'Straftat': straftat, 'erfasste Faelle': value} for straftat, value in result.items()]

    with open('aufgabe1-2.csv', "w", newline='', encoding='ISO-8859-1') as filter_output:

        fieldnames = ["Straftat","erfasste Faelle"]

        writer = csv.DictWriter(filter_output, fieldnames=fieldnames, extrasaction='ignore', delimiter=";")
        writer.writeheader()

        for line in bundesweite_liste:
            writer.writerow(line)

    print("Aufgabe 1-2.csv wurde exportiert.")



def sorted_bundesweite_berechnung():

    sorted_liste = sorted(bundesweite_liste, key=lambda k: k['erfasste Faelle'], reverse=True)

    with open('aufgabe1-3.csv', "w", newline='', encoding='ISO-8859-1') as filter_output:

        fieldnames = ["Straftat","erfasste Faelle"]

        writer = csv.DictWriter(filter_output, fieldnames=fieldnames, extrasaction='ignore', delimiter=";")
        writer.writeheader()

        for line in sorted_liste:
            writer.writerow(line)

    print("Aufgabe 1-3.csv wurde exportiert.")


def suche_nach_daten():

    while True:
        try:

            print("\nBitte geben Sie folgende Suchfelder ein:")
            print("\n1 - Schluesse "
                  "\n2 - Straftat"
                  "\n3 - Gemeindeschluessel"
                  "\n4 - Stadt-/Landkreis"
                  "\n5 - Kreisart"
                  "\n6 - erfasste Faelle"
                  "\n7 - HZ nach Zensus"
                  "\n8 - Versuche - Anzahl"
                  "\n9 - Versuche - Anteil in %"
                  "\n10 - mit Schusswaffe gedroht"
                  "\n11 - mit Schusswaffe geschossen"
                  "\n12 - aufgeklaerte Faelle"
                  "\n13 - Aufklaerungsquote"
                  "\n14 - Tatverdaechtige insgesamt"
                  "\n15 - Tatverdaechtige - maennlich"
                  "\n16 - Tatverdaechtige - weiblich"
                  "\n17 - Nichtdeutsche Tatverdaechtige - Anzahl"
                  "\n18 - Nichtdeutsche Tatverdaechtige - Anteil in %")


            navigation_eingabe = int(input("\nBitte geben Sie die Menü Zahl ein:"))

            if navigation_eingabe == 1:
                searcher("Schluesse")

            elif navigation_eingabe == 2:
                searcher("Straftat")

            elif navigation_eingabe == 3:
                searcher("Gemeindeschluessel")

            elif navigation_eingabe == 4:
                searcher("Stadt-/Landkreis")

            elif navigation_eingabe == 5:
                searcher("Kreisart")

            elif navigation_eingabe == 6:
                searcher("erfasste Faelle")

            elif navigation_eingabe == 7:
                searcher("HZ nach Zensus")

            elif navigation_eingabe == 8:
                searcher("Versuche - Anzahl")

            elif navigation_eingabe == 9:
                searcher("Versuche - Anteil in %")

            elif navigation_eingabe == 10:
                searcher("mit Schusswaffe gedroht")

            elif navigation_eingabe == 11:
                searcher("mit Schusswaffe gedroht")

            elif navigation_eingabe == 12:
                searcher("aufgeklaerte Faelle")

            elif navigation_eingabe == 13:
                searcher("Aufklaerungsquote")

            elif navigation_eingabe == 14:
                searcher("Tatverdaechtige insgesamt")

            elif navigation_eingabe == 15:
                searcher("Tatverdaechtige - maennlich")

            elif navigation_eingabe == 16:
                searcher("Tatverdaechtige - weiblich")

            elif navigation_eingabe == 17:
                searcher("Nichtdeutsche Tatverdaechtige - Anzahl")

            elif navigation_eingabe == 18:
                searcher("Nichtdeutsche Tatverdaechtige - Anteil in %")

            else:
                pass
        except ValueError:
            print("Bitte nur Integer eingeben, die in der Menü aufgelistet sind.")


def searcher(val):

    print(val)
    print("Bitte geben Sie ihre Suchanfrage an:")
    search_value = input()

    match = [l for l in cleaned_list if l[val] == search_value]

    if any(d[val] == search_value for d in match):

        print("Möchten Sie die Ergebnisse in der Command-Line anzeigen oder als CSV Speichern?")
        csv_oder_cmd = int(input("1 - CSV , 2 - Command-Line anzeigen"))

        try:
            if csv_oder_cmd == 1:

                print("Bitte geben sie den erwünschten Dateinamen an:")
                datei_name = input()
                with open('{}.csv'.format(datei_name), "w", newline='', encoding='ISO-8859-1') as filter_output:

                    fieldnames = ["Schluesse","Straftat", "Gemeindeschluessel", "Stadt-/Landkreis", "Kreisart", "erfasste Faelle", "HZ nach Zensus", "Versuche - Anzahl",
                                  "Versuche - Anteil in %", "mit Schusswaffe gedroht", "mit Schusswaffe geschossen", "aufgeklaerte Faelle", "Aufklaerungsquote",
                                  "Tatverdaechtige insgesamt", "Tatverdaechtige - maennlich", "Tatverdaechtige - weiblich",
                                  "Nichtdeutsche Tatverdaechtige - Anzahl", "Nichtdeutsche Tatverdaechtige - Anteil in %" ]

                    writer = csv.DictWriter(filter_output, fieldnames=fieldnames, extrasaction='ignore', delimiter=";")
                    writer.writeheader()

                    for matches in match:
                        writer.writerow(matches)
                print("CSV wurde exportiert.")

            elif csv_oder_cmd == 2:
                for matches in match:
                    print(matches)
            else:
                print("Bitte nur 1 oder 2 eingeben.")

        except ValueError:
            print("Bitte nur ganze Zahlen 1-2 eingeben.")


    else:
        print(search_value, "wurde nicht gefunden.")
    return match


import_csv()
#bundesweite_berechnung()
#sorted_bundesweite_berechnung()
suche_nach_daten()

