<<<<<<< HEAD
import urllib.request
import urllib.parse
LOGIN_URL='http://example.webscraping.com/usr/login'
LOGIN_EMAIL='amosawy123@163.com'
LOGIN_PASSWORD='ai794613'
data={'email':LOGIN_EMAIL,'password':LOGIN_PASSWORD}
encoded_data=urllib.parse.urlencode(data).encode(encoding='utf-8')
print(encoded_data)
request=urllib.request.Request(LOGIN_URL,encoded_data)
response=urllib.request.urlopen(request)
print(response.geturl())
print(response.code)

print(response.read().decode('utf-8'))
=======


# from PySide

import json

from simple.MongoDB import MongoCache
from simple.downloader import Downloader

cache=MongoCache()
D=Downloader(cache=cache)
url='http://example.webscraping.com/places/ajax/search.json?&search_term=.&page_size=500&page=0'
a=json.loads(D(url).decode('utf-8'))['num_pages']
print(a)
>>>>>>> 6a7bf5f2de02742b0b45a14f5d8eec3b102b176d
