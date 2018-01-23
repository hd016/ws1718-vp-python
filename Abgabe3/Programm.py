from lxml import etree
from copy import deepcopy
import json
from blitzdb import Document, FileBackend

# Xml FilePath
file_path = "dblp-2017-05-02.xml"

# Für BlitzDB
class Inproceedings(Document):
    pass


class Proceedings(Document):
    pass


backend = FileBackend("./dblp-db")
# Ende BlitzDb



def hauptmenu():
    print("\nBitte wählen Sie aus folgenden Punkten:")

    while True:
        print("\n--Hauptmenü--")
        print(
            "\n1 - Teilaufgabe 1.1"
            "\n2 - Teilaufgabe 1.2"
            "\n3 - Teilaufgabe 1.3"
            "\n4 - Teilaufgabe 2.1"
            "\n5 - Teilaufgabe 2.2"
            "\n6 - Exit")
        print("\nGeben Sie bitte ein:")
        try:
            hauptmenu_input = int(input())
        except Exception as e:
            print(str(e))
            hauptmenu()

        if hauptmenu_input == 1:
            teilaufgabe1_1()
        if hauptmenu_input == 2:
            teilaufgabe1_2()
        if hauptmenu_input == 3:
            teilaufgabe1_3()
        if hauptmenu_input == 4:
            teilaufgabe2_1()
        if hauptmenu_input == 5:
            teilaufgabe2_2()
        if hauptmenu_input == 6:
            exit()
            break

# Fertig - läuft.
def teilaufgabe1_1():
    countInproceedings = 0
    countProceedings = 0
    countJournals = 0

    for event, element in etree.iterparse(file_path, load_dtd=True):
        if element.tag == 'inproceedings':
            countInproceedings += 1
            if event == "end":
                element.clear()

        if element.tag == 'proceedings':
            countProceedings += 1
            if event == "end":
                element.clear()

        if element.tag == 'journal':
            countJournals += 1
            if event == "end":
                element.clear()

    print("inproceedings: ", countInproceedings,
          "proceedings: ", countProceedings,
          "journal: ", countJournals)


# To-Do: Überprüfen ob XML valide ist und XMl nicht richtig eingerückt, warum auch immer
def teilaufgabe1_2():
    countInproceedings = 0
    countProceedings = 0

    treeInproceedings = etree.Element("dblp")
    treeProceedings = etree.Element("dblp")

    for event, element in etree.iterparse(file_path, load_dtd=True):
        if element.tag == 'inproceedings':
            if (countInproceedings < 3):
                treeInproceedings.append(deepcopy(element))
                countInproceedings += 1
            if event == "end":
                element.clear()

        if element.tag == 'proceedings':
            if (countProceedings < 3):
                treeProceedings.append(deepcopy(element))
                countProceedings += 1
            if event == "end":
                element.clear()

        if (countInproceedings == 3 and countProceedings == 3):
            break

    # Export als XML
    try:
        baumIn = etree.ElementTree(treeInproceedings)
        baumIn.write('sample_inproceedings.xml', pretty_print=True, xml_declaration=True, encoding='ISO-8859-1',
                     method="xml")
    except (Exception):
        print("Fehler beim exportieren der XML." + Exception)
        hauptmenu()

    try:
        baumPro = etree.ElementTree(treeProceedings)
        baumPro.write('sample_proceedings.xml', pretty_print=True, xml_declaration=True, encoding='ISO-8859-1',
                      method="xml")
    except (Exception):
        print("Fehler beim exportieren der XML." + Exception)
        hauptmenu()


# Export als JSON von Inproceedings und Proceedings Elementen
def teilaufgabe1_3():
    inproceedingsList = []
    proceedingsList = []

    countInproceedings = 0
    countProceedings = 0

    for event, element in etree.iterparse(file_path, load_dtd=True):
        if element.tag == 'inproceedings':
            if (countInproceedings < 3):

                mdate = element.get("mdate")
                key = element.get("key")
                author = []
                title = ""
                pages = ""
                year = ""
                booktitle = ""
                ee = ""
                crossref = ""
                url = ""

                for e in element.iter():
                    if (e.tag == "author"):
                        author.append(e.text)
                    if (e.tag == "title"):
                        title = e.text
                    if (e.tag == "pages"):
                        pages = e.text
                    if (e.tag == "year"):
                        year = e.text
                    if (e.tag == "booktitle"):
                        booktitle = e.text
                    if (e.tag == "ee"):
                        ee = e.text
                    if (e.tag == "crossref"):
                        crossref = e.text
                    if (e.tag == "url"):
                        url = e.text

                inproceedings = {
                    'key': key,
                    'mdate': mdate,
                    'author': author,
                    'title': title,
                    'pages': pages,
                    'year': year,
                    'booktitle': booktitle,
                    'ee': ee,
                    'crossref': crossref,
                    'url': url
                }

                inproceedingsList.append(inproceedings)

                countInproceedings += 1
            if event == "end":
                element.clear()

        if element.tag == 'proceedings':
            if (countProceedings < 3):

                mdate = element.get("mdate")
                key = element.get("key")
                editor = []
                title = ""
                volume = ""
                year = ""
                isbn = ""
                booktitle = ""
                series = ""
                publisher = ""
                url = ""

                for e in element.iter():
                    if (e.tag == "editor"):
                        editor.append(e.text)
                    if (e.tag == "title"):
                        title = e.text
                    if (e.tag == "volume"):
                        volume = e.text
                    if (e.tag == "year"):
                        year = e.text
                    if (e.tag == "isbn"):
                        isbn = e.text
                    if (e.tag == "booktitle"):
                        booktitle = e.text
                    if (e.tag == "series"):
                        series = e.text
                    if (e.tag == "publisher"):
                        publisher = e.text
                    if (e.tag == "url"):
                        url = e.text

                proceedings = {
                    'key': key,
                    'mdate': mdate,
                    'editor': editor,
                    'title': title,
                    'volume': volume,
                    'year': year,
                    'isbn': isbn,
                    'booktitle': booktitle,
                    'series': series,
                    'publisher': publisher,
                    'url': url
                }

                proceedingsList.append(proceedings)

                countProceedings += 1
            if event == "end":
                element.clear()

        if (countInproceedings == 3 and countProceedings == 3):
            break

    # Export
    try:
        with open('sample_inproceedings.json', 'w', encoding='ISO-8859-1') as outfile:
            json.dump(inproceedingsList, outfile, indent=4)
    except (Exception):
        print("Fehler beim speichern als JSON." + Exception)
        hauptmenu()

    try:
        with open('sample_proceedings.json', 'w', encoding='ISO-8859-1') as outfile:
            json.dump(proceedingsList, outfile, indent=4)
    except (Exception):
        print("Fehler beim speichern als JSON." + Exception)
        hauptmenu()

# Evtl. nicht richtig für BlitzDB -> Dokumente verschieden benennen?
def teilaufgabe2_1():

    try:
        print("Parsing ...")
        parser = etree.XMLParser(dtd_validation=True)
        tree = etree.parse(file_path, parser)
        root = tree.getroot()
    except Exception:
        print(Exception)

    for e in root.xpath("./inproceedings[year='1980']"):
        mdate = e.get("mdate")
        key = e.get("key")
        author = []
        title = ""
        pages = ""
        year = ""
        booktitle = ""
        ee = ""
        crossref = ""
        url = ""

        for x in e.iter():
            if (x.tag == "author"):
                author.append(x.text)
            if (x.tag == "title"):
                title = x.text
            if (x.tag == "pages"):
                pages = x.text
            if (x.tag == "year"):
                year = x.text
            if (x.tag == "booktitle"):
                booktitle = x.text
            if (x.tag == "ee"):
                ee = x.text
            if (x.tag == "crossref"):
                crossref = x.text
            if (x.tag == "url"):
                url = x.text

        Inproc = Inproceedings({
            'key': key,
            'mdate': mdate,
            'author': author,
            'title': title,
            'pages': pages,
            'year': year,
            'booktitle': booktitle,
            'ee': ee,
            'crossref': crossref,
            'url': url
        })

        backend.save(Inproc)

        e.clear()

    for e in root.xpath("./proceedings"):

        mdate = e.get("mdate")
        key = e.get("key")
        editor = []
        title = ""
        volume = ""
        year = ""
        isbn = ""
        booktitle = ""
        series = ""
        publisher = ""
        url = ""

        for x in e.iter():
            if (x.tag == "editor"):
                editor.append(x.text)
            if (x.tag == "title"):
                title = x.text
            if (x.tag == "volume"):
                volume = x.text
            if (x.tag == "year"):
                year = x.text
            if (x.tag == "isbn"):
                isbn = x.text
            if (x.tag == "booktitle"):
                booktitle = x.text
            if (x.tag == "series"):
                series = x.text
            if (x.tag == "publisher"):
                publisher = x.text
            if (x.tag == "url"):
                url = x.text

        Proc = Proceedings({
            'key': key,
            'mdate': mdate,
            'editor': editor,
            'title': title,
            'volume': volume,
            'year': year,
            'isbn': isbn,
            'booktitle': booktitle,
            'series': series,
            'publisher': publisher,
            'url': url
        })

        backend.save(Proc)

        e.clear()

    # Commit, damit die Dokumente auf die Disc gespeichert werden
    backend.commit()

def teilaufgabe2_2():
    inproceedings = backend.filter(Inproceedings, {})

    for inproceeding in inproceedings:
        try:
            proceeding = backend.get(Proceedings, {'key' : inproceeding['crossref']})
            inproceeding['proc:editor'] = proceeding.editor
            inproceeding['proc:title'] = proceeding.title
            inproceeding['proc:volume'] = proceeding.volume
            inproceeding['proc:year'] = proceeding.year
            inproceeding['proc:isbn'] = proceeding.isbn
            inproceeding['proc:booktitle'] = proceeding.booktitle
            inproceeding['proc:series'] = proceeding.series
            inproceeding['proc:publisher'] = proceeding.publisher
            inproceeding['proc:url'] = proceeding.url

            inproceeding.save()

        except Proceedings.DoesNotExist:
            pass
        except Proceedings.MultipleDocumentsReturned:
            pass

    backend.commit()

def teilaufgabe3_1():
    print()



hauptmenu()