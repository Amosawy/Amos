from datetime import timedelta, datetime
from pymongo import MongoClient

from simple.AlexaCallback import AlexaCallback
from simple.MongoDB import MongoCache
from simple.scrapy import link_crawler


scrape_callback=AlexaCallback()
cache=MongoCache()
link_crawler(scrape_callback.seed_url,link_regex=None,scrape_callback=scrape_callback,cache=cache)
print()

