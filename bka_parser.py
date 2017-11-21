#Abgabe 1 Vertiefung Programmierung
#Autoren: Harun Dalici (29488), Tugay Yentur()

#######################
import sys          #
print(sys.version)  #
print("")           #
#####################

print("------ Bitte Python Version 3.5.x verwenden! Ab Version 3.5.x sind Dictionaries als Ordered Dict vordefiniert.! ----")
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
    '''Um die Codierung der CSV Datei richtig auslesen zu können, wird zuerst die ganze CSV Datei eingelesen
    und anschließend die Codierung in eine Dictionary gespeichert. Die Codierung befindet sich in der Variable result.
    @:param result['encoding]'''

    try:
        with open('tb01_FaelleGrundtabelleKreise_csv.csv', 'rb') as f:
            print("Bitte warten: Die Formatierung der CSV Datei wird ausgelesen..")
            global result
            result = chardet.detect(f.read())
            print("Die CSV Datei hat folgende Formatierung:", result)
    except Exception as e:
        print(str(e))

def import_csv():
    '''Die CSV Datei wird mit @:param result eingelesen. Die erste Zeile in der Datei wird komplett mit next() übersprungen.
    Anschließend wird überprüft, ob in der Spalte "Kreisart" sich Digits befinden, falls ja, wird diese Zeile *nicht* in die
    gesäuberte Liste eingelesen. Die Zeilen mit dem Inhalt "Straftaten insgesamt werden nicht berücksichtigt.'''

    try:
        with open('tb01_FaelleGrundtabelleKreise_csv.csv', encoding=result['encoding']) as csvfile:

            next(csvfile)

            faelle = [{k: v for k, v in row.items()}

            for row in csv.DictReader(csvfile, delimiter=";")]

            global cleaned_list
            cleaned_list = [line for line in faelle if not line["Kreisart"].isdigit() and not "Straftaten insgesamt" in line["Straftat"]]


        print("Die CSV wurde erfolgreich importiert.")

    except Exception as e:
        print(str(e))

def filter_list():
    '''Aufgabe 1-1 - Output: Aufgabe1-1.csv'''

    filtered_list = [row for row in cleaned_list if "LK" in row["Kreisart"] and float(row["Aufklaerungsquote"]) < 50 and not "Straftaten insgesamt" in row["Straftat"]]

    try:
        with open('aufgabe1-1.csv', "w", newline='', encoding=result['encoding']) as filter_output:

            fieldnames = ["Stadt-/Landkreis","Straftat","Aufklaerungsquote"]

            writer = csv.DictWriter(filter_output, fieldnames=fieldnames, extrasaction='ignore', delimiter=";")
            writer.writeheader()

            for line in filtered_list:
                writer.writerow(line)

        print("Aufgabe 1-1.csv wurde exportiert.")
    except Exception as e:
        print(str(e))

def bundesweite_berechnung():
    '''Aufgabe 1-2 - defaultdict <-> OrderedDict. Je nach Version und Ansatz kann zwischen diesen zwei Möglichkeiten entschieden werden.
    Die "erfasste Faelle" Spalte wird iteriert und anschließend mit dem results dictionary gemappt.'''

    berechnen_list = [row for row in cleaned_list if row["erfasste Faelle"].isdigit() and not "Straftaten insgesamt" in row["Straftat"]]

    results = defaultdict(int)

    for d in berechnen_list:
        results[d['Straftat']] += int(d['erfasste Faelle'])

    bundesweite_liste = [{'Straftat': straftat, 'Summe': value} for straftat, value in results.items()]

    try:
        with open('aufgabe1-2.csv', "w", newline='', encoding=result['encoding']) as filter_output:

            fieldnames = ["Straftat","Summe"]

            writer = csv.DictWriter(filter_output, fieldnames=fieldnames, extrasaction='ignore', delimiter=";")
            writer.writeheader()

            for line in bundesweite_liste:
                writer.writerow(line)

        print("Aufgabe 1-2.csv wurde exportiert.")

    except Exception as e:
        print(str(e))


def sorted_bundesweite_berechnung():
    '''Aufgabe 1-3 - Die bundesweite_liste wird in dieser Methode nach den erfassten Fällen sortiert.
    Die Keys werden mit dem Standard sorted Methode sortiert.'''

    sorted_liste = []

    berechnen_list = [row for row in cleaned_list if row["erfasste Faelle"].isdigit() and not "Straftaten insgesamt" in row["Straftat"]]

    results = defaultdict(int)

    for d in berechnen_list:
        results[d['Straftat']] += int(d['erfasste Faelle'])

    global bundesweite_liste
    bundesweite_liste = [{'Straftat': straftat, 'erfasste Faelle': value} for straftat, value in results.items()]

    try:
        sorted_liste = sorted(bundesweite_liste, key=lambda k: k['erfasste Faelle'], reverse=True)

    except NameError as e:
        print("Die Liste bundesweite_liste existiert nicht.")
        print("Error:", str(e))

    try:
        with open('aufgabe1-3.csv', "w", newline='', encoding=result['encoding']) as filter_output:

            fieldnames = ["Straftat","erfasste Faelle"]

            writer = csv.DictWriter(filter_output, fieldnames=fieldnames, extrasaction='ignore', delimiter=";")
            writer.writeheader()

            for line in sorted_liste:
                writer.writerow(line)

        print("Aufgabe 1-3.csv wurde exportiert.")
    except Exception as e:
        print(str(e))


def suche_nach_daten():
    '''Aufgabe 2-1 - Durch die Menüauswahl werden die Spaltennamen an die Methode searcher übergeben.'''

    while True:
        try:
            print("\nDatensuche Menü")
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
                print("Fehler. Bitte versuchen Sie es erneut.")
        except ValueError:
            print("Bitte nur Integer eingeben, die in der Menü aufgelistet sind.")


def searcher(val):
    '''In dieser Methode wird durch eine List Comphrension die gematchen Zeilen in eine neue Liste geschrieben. Anschließend wird die Methode
    print_oder_csv aufgerufen. '''

    print(val)
    print("Bitte geben Sie ihre Suchanfrage an:")

    search_value = ""

    try:
        search_value = input()
    except Exception as e:
        print(str(e))

    match = [l for l in cleaned_list if l[val] == search_value]

    if any(d[val] == search_value for d in match):
        print_or_csv(match)

    else:
        print(search_value, "wurde nicht gefunden.")
    return match


def filter_values():
    '''Aufgabe 2-2 - Es werden zwei Werte (val1, val2) angenommen und anschließend an die Methode filterer übergeben.'''

    global val1
    global val2


    menu_dict = {"Gemeindeschluessel":1, "erfasste Faelle":2,  "HZ nach Zensus":3, "Versuche - Anzahl":4, "Versuche - Anteil in %":5,
                     "mit Schusswaffe gedroht":6, "mit Schusswaffe geschossen":7, "aufgeklaerte Faelle":8, "Aufklaerungsquote":9, "Tatverdaechtige insgesamt":10,
                     "Tatverdaechtige - maennlich": 11, "Tatverdaechtige - weiblich":12,
                     "Nichtdeutsche Tatverdaechtige - Anzahl":13, "Nichtdeutsche Tatverdaechtige - Anteil in %":14 }

    menu_liste = sorted([(value,key) for (key,value) in menu_dict.items()])

    for item in menu_liste :
        print(item)

    print("\nWelche numerische Felder möchten Sie filtern?")

    print("\nGeben Sie das Feld 1 an:")
    input_val1 = 0

    try:

        input_val1 = int(input())

    except ValueError:
        print("Bitte nur Integer eingeben.")
        filter_values()

    input_val1 += -1


    try:
        val1 = menu_liste[input_val1][1]
        print(val1)

    except IndexError as e:
        print("Bitte nur Zahlen im Menü angeben.",str(e))
        filter_values()


    print("\nGeben Sie das Feld 2 an:")
    input_val2 = 0

    try:
        input_val2 = int(input())

    except ValueError:
        print("Bitte nur Integer eingeben.")
        filter_values()

    input_val2 += -1

    try:
        val2 = menu_liste[input_val2][1]
        print(val2)

    except IndexError as e:
        print("Bitte nur Zahlen im Menü angeben.",str(e))
        filter_values()

    print("\nSie haben folgende Felder zum Filtern ausgesucht:")
    print(val1, "," , val2)

    filterer()


def filterer():
    '''Die ausgewählten Wertenamen (val1,val2) werden nun mit wert1 und wert2 "gemappt". Es werden zwei neue Listen je advanced_filtered_list erstellt.
    Durch die If-Menü werden die Operatoren und dessen Attribute übergeben. ineq1 sowie ineq2 sind Operator Variablen, die als Strings gespeichert werden.
    gt = greater then, lt = little then, eq = equal. Je Durchlauf wird durch die If-Menü die Operatoren neuzugeordnet. Anschließend bekommen die
    zwei advanced_filtered_lists mit List Comprehnsions neue Daten zugewießen. Anschließend werden diese zwei Maps an die nächste Funktion zum
    Mappen übergeben. Dort werden die logischen Operatoren angewendet.'''

    global wert1, wert2
    global ineq_1, ineq_2

    global advanced_filtered_list_val1
    advanced_filtered_list_val1 = []

    global advanced_filtered_list_val2
    advanced_filtered_list_val2 = []

    print("\nMit Welchen Wert möchten Sie das Erste Feld filtern?")

    try:
        wert1 = int(input())

    except ValueError as e:
        print("Bitte nur Integer oder Float eingeben. Diese Datensuche bietet nur numerische Suchen an.", str(e))
        print("Funktion Reset")
        filterer()

    print("\nWelchen Operator möchten Sie verwnden?")
    print("\n1 - <"
          "\n2 - >"
          "\n3 - =")

    operatoren_auswahl = 0

    try:
        operatoren_auswahl = int(input())

        if operatoren_auswahl not in range(1,4):
            print("Bitte 1, 2 oder 3 eingeben")
            print("Funktion Reset")
            filterer()

    except (ValueError, TypeError, IndexError, KeyError) as e:
        print(str(e))
        filterer()


    if operatoren_auswahl == 1:
        advanced_filtered_list_val1 = [tuple(row.items()) for row in cleaned_list if float(row[val1]) < wert1]
        ineq_1 = 'gt'

    elif operatoren_auswahl == 2:
        advanced_filtered_list_val1 = [tuple(row.items()) for row in cleaned_list if float(row[val2]) > wert1]
        ineq_1 = 'lt'

    elif operatoren_auswahl == 3:
        advanced_filtered_list_val1 = [tuple(row.items()) for row in cleaned_list if float(row[val2]) == wert1]
        ineq_1 = 'eq'


    print("\nMit Welchen Wert möchten Sie das Zweite Feld filtern?")

    try:
        wert2 = int(input())

    except ValueError as e:
        print("Bitte nur Integer oder Float eingeben. Diese Datensuche bietet nur numerische Suchen an.", str(e))
        print("Funktion Reset")
        filterer()


    print("\nWelchen Operator möchten Sie verwnden?")
    print("\n1 - <"
          "\n2 - >"
          "\n3 - =")

    operatoren_auswahl = 0

    try:
        operatoren_auswahl = int(input())

        if operatoren_auswahl not in range(1,4):
            print("Bitte 1, 2 oder 3 eingeben")
            print("Funktion Reset")
            filterer()

    except (ValueError, TypeError, IndexError, KeyError) as e:
        print(str(e))
        filterer()

    if operatoren_auswahl == 1:
        advanced_filtered_list_val2 = [tuple(row.items()) for row in cleaned_list if float(row[val2]) < wert2]
        ineq_2 = 'gt'

    elif operatoren_auswahl == 2:
        advanced_filtered_list_val2 = [tuple(row.items()) for row in cleaned_list if float(row[val2]) > wert2]
        ineq_2 = 'lt'

    elif operatoren_auswahl == 3:
        advanced_filtered_list_val2 = [tuple(row.items()) for row in cleaned_list if float(row[val2]) == wert2]
        ineq_2 = 'eq'


    map_filters(advanced_filtered_list_val1,advanced_filtered_list_val2)


def map_filters(list1, list2):
    '''Durch die If-Menü werden zwei je nach operatoren_auswahl lambda Funktionen aufgerufen. Durch getattr Funktion werden die Operatoren
    Attribute angewandt (gt, lt, eq).'''

    print("\nMit Welchen logischen Operatoren möchten Sie die Felder filtern?")
    print("\n1 - &"
          "\n2 - |")

    operatoren_auswahl = 0

    try:
        operatoren_auswahl = int(input())

        if operatoren_auswahl not in range(1,3):
            print("Bitte 1 oder 2 eingeben")
            print("Funktion Reset")
            map_filters(advanced_filtered_list_val1,advanced_filtered_list_val2)

    except (ValueError, TypeError, IndexError, KeyError) as e:
        print(str(e))
        print("Funktion Reset")
        map_filters(advanced_filtered_list_val1,advanced_filtered_list_val2)

    andor = {
        1:lambda L: filter(lambda d:getattr(op,ineq_1)(float(d[val1]), wert1) and getattr(op,ineq_2)(float(d[val2]), wert2), L),
        2:lambda L: filter(lambda d:getattr(op,ineq_1)(float(d[val1]), wert1) or  getattr(op,ineq_2)(float(d[val2]), wert2), L),}

    mapped_list = []

    try:
        mapped_list = andor[operatoren_auswahl](cleaned_list)

    except (ValueError, TypeError, IndexError, KeyError) as e:
        print(str(e))
    print_or_csv(mapped_list)


def print_or_csv(match):
    '''Die Methode wird aufgerufen für die Möglichkeit zwischen CSV oder Command-Line Output. Der User kann den datei_name selbst wählen.'''

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

    while True:
        print("\n--Hauptmenü--")
        print("\n1 - Teilaufgabe 1 - Landkreise filtern"
          "\n2 - Teilaufgabe 1 - Berechnung für ganz Deutschland"
          "\n3 - Teilaufgabe 1 - Berechnung sortieren"
          "\n4 - Teilaufgabe 2 - Suche nach Daten"
          "\n5 - Teilaufgabe 2 - Filtern von Daten"
          "\n6 - Exit")
        print("\nGeben Sie bitte ein:")
        try:
            hauptmenu_input = int(input())
        except Exception as e:
            print(str(e))
            hauptmenu()

        if hauptmenu_input == 1:
            filter_list()
        if hauptmenu_input == 2:
            bundesweite_berechnung()
        if hauptmenu_input == 3:
            sorted_bundesweite_berechnung()
        if hauptmenu_input == 4:
            suche_nach_daten()
        if hauptmenu_input == 5:
            filter_values()
        if hauptmenu_input == 6:
            exit()
            break

encoder()
import_csv()
hauptmenu()
