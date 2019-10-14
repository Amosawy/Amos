

# from PySide

import json

from simple.MongoDB import MongoCache
from simple.downloader import Downloader

cache=MongoCache()
D=Downloader(cache=cache)
url='http://example.webscraping.com/places/ajax/search.json?&search_term=.&page_size=500&page=0'
a=json.loads(D(url).decode('utf-8'))['num_pages']
print(a)