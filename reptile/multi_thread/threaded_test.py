from multi_thread.AlexaCallback import AlexaCallback
from multi_thread.threaded_Crawler import threaded_crawler
from simple.MongoDB import MongoCache


def main(maxthreads):
    scrape_callback=AlexaCallback()
    cache=MongoCache()
    threaded_crawler(scrape_callback.seed_url,max_threads=maxthreads,scrape_callback=scrape_callback,cache=cache)
if __name__ == '__main__':
    main(5)