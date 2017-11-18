#Aufgabe 1 einlesen
#####################
import sys          #
print(sys.version)  #
print("")           #
#####################

print("------ Bitte Python Version 3.5.x verwenden! Ab Version 3.5.x werden geschriebene Dictionaries aus writedict als ordered dict gespeichert! ----")

#################################
# Modul Importe                 #
import csv                      #
import pandas as pd             #
import chardet                  #
import re                       #
from collections import defaultdict
import functools                #
#################################


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
        cleaned_list = [line for line in faelle if not line["Kreisart"].isdigit()]


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



import_csv()
bundesweite_berechnung()
sorted_bundesweite_berechnung()

