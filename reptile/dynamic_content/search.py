import csv
import json
import string
from pprint import pprint

from simple.MongoDB import MongoCache
from simple.downloader import Downloader
cache=MongoCache()
D=Downloader(cache=cache)
template_url='http://example.webscraping.com/places/ajax/search.json?&search_term={}&page_size=10&page={}'
countries=set()
for letter in string.ascii_lowercase:
    page=0
    while True:
        html=D(template_url.format(letter,page))
        try:
            ajax=json.loads(html.decode('utf-8'))
        except ValueError as e:
            print(e)
            ajax=None
        else:
            for record in ajax['records']:
                countries.add(record['country'])
        page+=1
        if ajax is None or page>=ajax['num_pages']:
            break
pprint(countries)
print(len(countries))