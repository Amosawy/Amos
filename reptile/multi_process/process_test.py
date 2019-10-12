import sys

from multi_process.process_crawler import process_crawler
from multi_thread.AlexaCallback import AlexaCallback
from simple.MongoDB import MongoCache


def main(max_threads):
    scrape_callback=AlexaCallback()
    cache=MongoCache()
    process_crawler(scrape_callback.seed_url,scrape_callback=scrape_callback,cache=cache,max_threads=max_threads)
if __name__ == '__main__':
    max_threads=5
    main(max_threads)