import multiprocessing
import threading
import time

from multi_process.Mongo_queue import MongoQueue
from simple.downloader import Downloader

SLEEP_TIME=1
def threaded_crawler(seed_url,cache=None,scrape_callback=None,user_agent='wswp',max_threads=10,timeout=60):
    crawl_queue=MongoQueue()
    crawl_queue.clear()
    crawl_queue.push(seed_url)
    D=Downloader(cache=cache,user_agent=user_agent)
    def process_queue():
        while True:
            # keep track that are processing url
            try:
                url=crawl_queue.pop()
            except KeyError:
                print("current no urls to process")
                break
            else:
                html=D(url)
                if scrape_callback:
                    try:
                        links=scrape_callback(url,html) or []
                    except Exception as e:
                        print('Error in callback for:{}:{}'.format(url,e))
                    else:
                        for link in links:
                            crawl_queue.push(link)
                crawl_queue.complete(url)
    threads=[]
    while threads or crawl_queue:
        for thread in threads:
            if not  thread.is_alive():
                threads.remove(thread)
        while len(threads)<max_threads and crawl_queue:
            thread=threading.Thread(target=process_queue)
            thread.setDaemon(True)
            thread.start()
            threads.append(thread)
        time.sleep(SLEEP_TIME)
def process_crawler(args,**kwargs):
    num_cpus=multiprocessing.cpu_count()
    print('start {} processes'.format(num_cpus))
    processes=[]
    for i in range(num_cpus):
        p=multiprocessing.Process(target=threaded_crawler,args=[args],kwargs=kwargs)
        p.start()
        processes.append(p)
    for p in processes:
        p.join()

