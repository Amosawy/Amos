from pprint import pprint
from urllib import parse

from simple.downloader import Downloader


def link_crawler(seed_url,max_threads=10,depth_max=-1,scrape_callback=None,user_agent='wswp',cache=None):
    crawl_queue=[seed_url]
    seen={seed_url: 0}
    D=Downloader(user_agent=user_agent,cache=cache)
    def process_queue():
        while True:
            try:
                url=crawl_queue.pop()
            except IndexError:
                # crawl_queue is empty
                break
            else:
                html=D(url)
                if scrape_callback:
                    links=scrape_callback(url,html) or []


