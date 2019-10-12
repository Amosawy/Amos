from datetime import datetime, timedelta

from multi_thread.AlexaCallback import AlexaCallback
from simple.MongoDB import MongoCache
from simple.scrapy import link_crawler


# scrape_callback=AlexaCallback()
# cache=MongoCache()
# link_crawler(scrape_callback.seed_url,link_regex=None,scrape_callback=scrape_callback,cache=cache)
def main():
    timeout=300
    print(datetime.now())
    print(timedelta(seconds=timeout))
    print(datetime.now()-timedelta(seconds=timeout))
if __name__ == '__main__':
    main()