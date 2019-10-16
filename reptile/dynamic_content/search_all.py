import csv
import json

from simple.MongoDB import MongoCache
from simple.downloader import Downloader
cache=MongoCache()
D=Downloader(cache=cache)
Fields={'country'}
writer=csv.writer(open('countries.csv','w'))
writer.writerow(Fields)
html=D('http://example.webscraping.com/places/ajax/search.json?&search_term=.&page_size=500&page=0')
ajax=json.loads(html.decode('utf-8'))
for record in ajax['records']:
    row=[record[field] for field in Fields]
    print(row)
    writer.writerow(row)