#Aufgabe 1 einlesen
#####################
import sys          #
print(sys.version)
print("")
print("------ Bitte Python Version 3.5.x verwenden! Ab Version 3.5.x werden geschriebene Dictionaries aus writedict als ordered dict gespeichert! ----")#
#####################

#####################
# Modul Importe     #
import csv          #
import pandas as pd #
import chardet      #
import re           #
#####################


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

        global row
        faelle = [{k: v for k, v in row.items()}

        for row in csv.DictReader(csvfile, delimiter=";")]

        global cleaned_list
        cleaned_list = [row for row in faelle if not row["Kreisart"].isdigit()]

        #for row in cleaned_list:
         #   print(row)


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

#encoder() if you need encoder() then -> with open encoding=result["encoding"]
import_csv()
