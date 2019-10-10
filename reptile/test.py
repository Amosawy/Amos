from multi_thread.AlexaCallback import AlexaCallback
from simple.MongoDB import MongoCache
from simple.scrapy import link_crawler


# scrape_callback=AlexaCallback()
# cache=MongoCache()
# link_crawler(scrape_callback.seed_url,link_regex=None,scrape_callback=scrape_callback,cache=cache)
def main():
    a, b, c = range(3)
    print(a, b, c)
if __name__ == '__main__':
    main()