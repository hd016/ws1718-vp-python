import json
import urllib2


'''Aus Kompatibilitaetsgruenden wurde hier auf Python 2 umgestiegen. Da sich aktuell mit Python3 die Europeana API mit der Standard
Library Urllib nicht trivial umsetzen laesst.'''

outfile = open('5213europeana233.csv', 'w')

outfile.write("Element, Title, Land")
outfile.write("\n")

response = json.load(urllib2.urlopen("http://www.europeana.eu/api/v2/search.json?start=1&rows=10&wskey=dpLszRsbx&query=(mozart+OR+beethoven+OR+berlin)"))

element_counter = 0

# Loop
for item in response["items"]:

    element_counter += 1

    outfile.write("Element: " + str(element_counter)+",")

    outfile.write(item["title"][0].encode('utf-8').replace(",", "") + ",")

    outfile.write(item["country"][0] + ",")

    outfile.write("\n")

outfile.close()

element_counter = 0


for item in response["items"]:
    element_counter += 1

    print "Element: " + str(element_counter)+",", "Title: ", item["title"][0].encode('utf-8'),",", "Land: ", str(item["country"][0]).capitalize() + ","
