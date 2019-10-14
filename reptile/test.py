from datetime import datetime, timedelta

import lxml.html
from lxml import etree
from multi_thread.AlexaCallback import AlexaCallback
from simple.MongoDB import MongoCache
from simple.downloader import Downloader
from simple.scrapy import link_crawler


# scrape_callback=AlexaCallback()
# cache=MongoCache()
# link_crawler(scrape_callback.seed_url,link_regex=None,scrape_callback=scrape_callback,cache=cache)
def main():
    D=Downloader()
    html=D('http://example.webscraping.com/places/default/search')
    print(html.decode('utf-8'))
    tree=lxml.html.fromstring(html)
    a=tree.xpath('//*[@id="results"]/table/tbody/tr[1]/td[1]/div/a/text()')
    print(a)
if __name__ == '__main__':
    main()