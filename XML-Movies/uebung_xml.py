import xml.etree.ElementTree as ET
import collections

def import_movies():
    try:
        tree = ET.parse('movies.xml')
        global root
        root = tree.getroot()
        print("Datei erfolgreich geladen.")
    except Exception as e:
        print(str(e))

def hauptmenu():
    print("\nBitte Wählen Sie aus folgenden Punkten:")

    while True:
        print("\n1 - Aufgabe 1 - Titel, Regisseur und Jahr"
          "\n2 - Aufgabe 2 - Filme aus den Jahren 2000-2010"
          "\n3 - Aufgabe 3 - Welche Genres sind enthalten"
          "\n4 - Aufgabe 4 - Welcher Regisseur taucht am häufigsten auf"
          "\n5 - Exit")
        print("\nGeben Sie bitte ein:")
        try:
            hauptmenu_input = int(input())
        except Exception as e:
            print(str(e))
            hauptmenu()

        if hauptmenu_input == 1:
            aufgabe1()
        if hauptmenu_input == 2:
            aufgabe2()
        if hauptmenu_input == 3:
            aufgabe3()
        if hauptmenu_input == 4:
            aufgabe4()
        if hauptmenu_input == 5:
            exit()
            break


def aufgabe1():
    try:

        for hit in iter(root):
            if(hit.tag == 'movie'):
                movieList = []
                for h in hit:
                    if(h.tag == 'title'):
                        movieList.append("Film: " + str(h.text) + " | ")
                    if(h.tag == 'producer'):
                        producer = ""
                        for p in h:
                            for j in p:
                                if(j.tag == 'name'):
                                    producer += str(j.text) + " - "
                        movieList.append(producer + "|")
                    if(h.tag == 'year'):
                        movieList.append("Jahr: " + str(h.text) + " | ")
                print(''.join(movieList))

    except Exception as e:
        print(str(e))

def aufgabe2():
    try:
        for hit in iter(root):
            if(hit.tag == 'movie'):
                for h in hit:
                    if(h.tag == 'year'):
                        year = int(h.text)
                        if(year >= 2000 and year <= 2010):
                            for t in hit:
                                if(t.tag == 'title'):
                                    print(year, t.text)
    except Exception as e:
        print(str(e))


def aufgabe3():
    try:
        genreList = []

        for hit in iter(root):
            if(hit.tag == 'movie'):
                for genres in hit:
                    if(genres.tag == 'genres'):
                        for genre in genres:
                            genreList.append(genre.text)

        # Löscht Elemente die mehr als einmal vorkommen und gibt die Liste aus
        print(list(set(genreList)))

    except Exception as e:
        print(str(e))

def aufgabe4():
    try:
        producerList = []
        for hit in iter(root):
            if(hit.tag == 'movie'):
                for h in hit:
                    if(h.tag == 'producer'):
                        for p in h:
                            for j in p:
                                if(j.tag == 'name'):
                                    producerList.append(j.text)

        counter = collections.Counter(producerList)
        print(counter.most_common(1))
    except Exception as e:
        print(str(e))

import_movies()
hauptmenu()
