#Aufgabe 1 einlesen
#####################
import sys          #
print(sys.version)  #
#####################

#####################
# Modul Importe     #
import csv          #
import pandas as pd #
import chardet      #
import re           #
#####################


faelle = []


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

        cleaned_list = [row for row in faelle if not row["Kreisart"].isdigit()]


        for row in cleaned_list:
            print(row)

    print("Die CSV wurde erfolgreich importiert.")

#encoder() if you need encoder() then -> with open encoding=result["encoding"]
import_csv()


