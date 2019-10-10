import threading
import time
from pprint import pprint
from urllib import parse

from simple.downloader import Downloader


def threaded_crawler(seed_url,max_threads=10,depth_max=-1,scrape_callback=None,user_agent='wswp',cache=None):
    crawl_queue=[seed_url]
    seen=set([seed_url])
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
                # 获取需要下载的链接
                if scrape_callback:
                    try:
                        links=scrape_callback(url,html) or []
                    except Exception as e:
                        print('Error in callback for:{}:{}'.format(url,e))
                    else:
                        for link in links:
                            if link not in seen:
                                seen.add(link)
                                crawl_queue.append(link)
    threads=[]
    while threads or crawl_queue:
        for thread in threads:
            if not thread.is_alive():
                # remove the stopped thread
                print("remove dead thread")
                threads.remove(thread)
        while len(threads) < max_threads and crawl_queue:
            # can start some more threads
            thread=threading.Thread(target=process_queue)
            thread.setDaemon(True)
            thread.start()
            threads.append(thread)
            print("create new thread")
        print(crawl_queue)
        print(len(threads))
        time.sleep(1)