#Abgabe 1 Vertiefung Programmierung
#Autoren: Harun Dalici (29488), Tugay Yentur()

#######################
import sys          #
print(sys.version)  #
print("")           #
#####################

print("------ Bitte Python Version 3.5.x verwenden! Ab Version 3.5.x werden sind Dictionaries als Ordered Dict vordefiniert.! ----")
print("")

#####################################
# Module #                          #
                                    #
import csv                          #
import chardet                      #
from collections import defaultdict #
import operator as op               #
#####################################


faelle = []

global row
row = {}

def encoder():

    with open('/Users/DHarun/PycharmProjects/Vertiefung-Programmierung/Abgabe1/tb01_FaelleGrundtabelleKreise_csv.csv', 'rb') as f:
        global result
        result = chardet.detect(f.read())
        print("Die CSV Datei hat folgende Formatierung:", result)

def import_csv():

    with open('/Users/DHarun/PycharmProjects/Vertiefung-Programmierung/Abgabe1/tb01_FaelleGrundtabelleKreise_csv.csv', encoding=result['encoding']) as csvfile:

        next(csvfile)

        faelle = [{k: v for k, v in row.items()}

        for row in csv.DictReader(csvfile, delimiter=";")]

        global cleaned_list
        cleaned_list = [line for line in faelle if not line["Kreisart"].isdigit() and not "Straftaten insgesamt" in line["Straftat"]]


    print("Die CSV wurde erfolgreich importiert.")


def filter_list():

    filtered_list = [row for row in cleaned_list if "LK" in row["Kreisart"] and float(row["Aufklaerungsquote"]) < 50 and not "Straftaten insgesamt" in row["Straftat"]]

    with open('aufgabe1-1.csv', "w", newline='', encoding=result['encoding']) as filter_output:

        fieldnames = ["Stadt-/Landkreis","Straftat","Aufklaerungsquote"]

        writer = csv.DictWriter(filter_output, fieldnames=fieldnames, extrasaction='ignore', delimiter=";")
        writer.writeheader()

        for line in filtered_list:
            writer.writerow(line)

    print("Aufgabe 1-1.csv wurde exportiert.")


def bundesweite_berechnung():

    berechnen_list = [row for row in cleaned_list if row["erfasste Faelle"].isdigit() and not "Straftaten insgesamt" in row["Straftat"]]

    results = defaultdict(int)

    for d in berechnen_list:
        results[d['Straftat']] += int(d['erfasste Faelle'])

    global bundesweite_liste
    bundesweite_liste = [{'Straftat': straftat, 'erfasste Faelle': value} for straftat, value in results.items()]

    with open('aufgabe1-2.csv', "w", newline='', encoding=result['encoding']) as filter_output:

        fieldnames = ["Straftat","erfasste Faelle"]

        writer = csv.DictWriter(filter_output, fieldnames=fieldnames, extrasaction='ignore', delimiter=";")
        writer.writeheader()

        for line in bundesweite_liste:
            writer.writerow(line)

    print("Aufgabe 1-2.csv wurde exportiert.")



def sorted_bundesweite_berechnung():

    sorted_liste = sorted(bundesweite_liste, key=lambda k: k['erfasste Faelle'], reverse=True)

    with open('aufgabe1-3.csv', "w", newline='', encoding=result['encoding']) as filter_output:

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
            print("\n0 - Zurück zur Hauptmenü"
                  "\n1 - Schluesse "
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

            if navigation_eingabe == 0:
                hauptmenu()

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
                print("napiyon amk.")
        except ValueError:
            print("Bitte nur Integer eingeben, die in der Menü aufgelistet sind.")


def searcher(val):

    print(val)
    print("Bitte geben Sie ihre Suchanfrage an:")
    search_value = input()

    match = [l for l in cleaned_list if l[val] == search_value]

    if any(d[val] == search_value for d in match):
        print_or_csv(match)

    else:
        print(search_value, "wurde nicht gefunden.")
    return match


def filtern_von_daten():

    menu_dict = {"Gemeindeschluessel":1, "erfasste Faelle":2,  "HZ nach Zensus":3, "Versuche - Anzahl":4, "Versuche - Anteil in %":5,
                     "mit Schusswaffe gedroht":6, "mit Schusswaffe geschossen":7, "aufgeklaerte Faelle":8, "Aufklaerungsquote":9, "Tatverdaechtige insgesamt":10,
                     "Tatverdaechtige - maennlich": 11, "Tatverdaechtige - weiblich":12,
                     "Nichtdeutsche Tatverdaechtige - Anzahl":13, "Nichtdeutsche Tatverdaechtige - Anteil in %":14 }

    menu_liste = sorted([(value,key) for (key,value) in menu_dict.items()])
    for item in menu_liste :
        print(item)

    print("\nWelche numerische Felder möchten Sie filtern?")

    print("\nGeben Sie das Feld 1 an:")
    input_val1 = int(input())
    global val1
    val1 = menu_liste [input_val1][1]
    print(val1)

    print("\nGeben Sie das Feld 2 an:")
    global val2
    input_val2 = int(input())
    val2 = menu_liste [input_val2][1]
    print(val2)

    print("\nSie haben folgende Felder zum Filtern ausgesucht:")
    print(val1, "," , val2)

    filterer(val1, val2)

def filterer(val1, val2):

    print("\nMit Welchen Wert möchten Sie das Erste Feld filtern?")
    global wert1
    wert1 = int(input())

    print("\nWelchen Operator möchten Sie verwnden?")
    print("\n1 - <"
          "\n2 - >"
          "\n3 - =")

    global ineq_1, ineq_2

    global advanced_filtered_list_val1
    advanced_filtered_list_val1 = []

    operatoren_auswahl = int(input())

    if operatoren_auswahl == 1:
        advanced_filtered_list_val1 = [tuple(row.items()) for row in cleaned_list if float(row[val1]) < wert1]
        ineq_1 = 'gt'

    elif operatoren_auswahl == 2:
        advanced_filtered_list_val1 = [tuple(row.items()) for row in cleaned_list if float(row[val2]) > wert1]
        ineq_1 = 'lt'

    elif operatoren_auswahl == 3:
        advanced_filtered_list_val1 = [tuple(row.items()) for row in cleaned_list if float(row[val2]) == wert1]
        ineq_1 = 'eq'

    else:
        print("Bitte nur 1-3 eingeben.")


    print("\nMit Welchen Wert möchten Sie das Zweite Feld filtern?")
    global wert2
    wert2 = int(input())

    print("\nWelchen Operator möchten Sie verwnden?")
    print("\n1 - <"
          "\n2 - >"
          "\n3 - =")

    operatoren_auswahl = int(input())

    global advanced_filtered_list_val2
    advanced_filtered_list_val2 = []


    if operatoren_auswahl == 1:
        advanced_filtered_list_val2 = [tuple(row.items()) for row in cleaned_list if float(row[val2]) < wert2]
        ineq_2 = 'gt'

    elif operatoren_auswahl == 2:
        advanced_filtered_list_val2 = [tuple(row.items()) for row in cleaned_list if float(row[val2]) > wert2]
        ineq_2 = 'lt'

    elif operatoren_auswahl == 3:
        advanced_filtered_list_val2 = [tuple(row.items()) for row in cleaned_list if float(row[val2]) == wert2]
        ineq_2 = 'eq'

    else:
        print("Bitte nur 1-3 eingeben.")

    map_filters(advanced_filtered_list_val1,advanced_filtered_list_val2)


def map_filters(list1, list2):
    print("\nMit Welchen logischen Operatoren möchten Sie die Felder filtern?")
    print("\n1 - &"
          "\n2 - |")

    operatoren_auswahl = int(input())


    andor = {
        1:lambda L: filter(lambda d:getattr(op,ineq_1)(float(d[val1]), wert1) and getattr(op,ineq_2)(float(d[val2]), wert2), L),
        2:lambda L: filter(lambda d:getattr(op,ineq_1)(float(d[val1]), wert1) or  getattr(op,ineq_2)(float(d[val2]), wert2), L),}

    mapped_list = andor[operatoren_auswahl](cleaned_list)
    print_or_csv(mapped_list)


def print_or_csv(match):

    print("Möchten Sie die Ergebnisse in der Command-Line anzeigen oder als CSV Speichern?")
    csv_oder_cmd = int(input("1 - CSV , 2 - Command-Line anzeigen"))

    try:
        if csv_oder_cmd == 1:
            print("Bitte geben sie den erwünschten Dateinamen an:")
            datei_name = input()
            with open('{}.csv'.format(datei_name), "w", newline='', encoding=result['encoding']) as filter_output:

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



###########################
# Start #
###########################


def hauptmenu():
    print("\nBitte Wählen Sie aus folgenden Punkten:")
    print("\n1 - Teilaufgabe 1 - Landkreise filtern"
          "\n2 - Teilaufgabe 1 - Berechnung für ganz Deutschland"
          "\n3 - Teilaufgabe 1 - Berechnung sortieren"
          "\n4 - Teilaufgabe 2 - Suche nach Daten"
          "\n5 - Teilaufgabe 2 - Filtern von Daten"
          "\n6 - Exit")

    while True:
        print("\nGeben Sie bitte ein:")
        hauptmenu_input = int(input())

        if hauptmenu_input == 1:
            filter_list()
        if hauptmenu_input == 2:
            bundesweite_berechnung()
        if hauptmenu_input == 3:
            sorted_bundesweite_berechnung()
        if hauptmenu_input == 4:
            suche_nach_daten()
        if hauptmenu_input == 5:
            filtern_von_daten()
        if hauptmenu_input == 6:
            exit()
            break

encoder()
import_csv()
hauptmenu()


