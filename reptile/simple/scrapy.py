import csv
import os
import pickle
import time
import urllib.request as urllib2
import re
import urllib.parse as parse
import zlib
from datetime import timedelta, datetime
from pprint import pprint
import cssselect
import lxml.html
from pymongo import MongoClient
from simple.downloader import Downloader
from simple.MongoDB import MongoCache
from simple.Scrapecallback import ScrapeCallback


# 链接爬虫
def link_crawler(seed_url,link_regex,depth_max=-1,scrape_callback=None,user_agent='wswp',cache=None):
    crawl_queue=[seed_url]
    seen={seed_url: 0}
    D=Downloader(user_agent=user_agent,cache=cache)
    while crawl_queue:
        url=crawl_queue.pop()
        html=D(url)
        links=[]
        depth=seen[url]
        if scrape_callback:
            links.extend(scrape_callback(url,html) or [])
        print(depth)
        if depth !=depth_max:
            links.extend(link for link in get_links(html.decode('utf-8')) if re.search(link_regex,link))
            pprint(links)
            for link in links:
                link=parse.urljoin(seed_url,link)
                if link not in seen:
                    seen[link]=depth+1
                    crawl_queue.append(link)
def get_links(html):
    webpage_regex=re.compile('<a[^>]+href=["\'](.*?)["\']',re.IGNORECASE)
    return webpage_regex.findall(html)

link_crawler('http://example.webscraping.com/','/(index|view)/',depth_max=1,scrape_callback=ScrapeCallback(),cache=MongoCache())

# 缓存到磁盘
# class DiskCache:
#     #
#     # >>> cache = DiskCache()
#     # >>> url = 'http://example.webscraping.com'
#     # >>> result = {'html': '...'}
#     # >>> cache[url] = result
#     # >>> cache[url]['html'] == result['html']
#     # True
#     # >>> cache = DiskCache(expires=timedelta())
#     # >>> cache[url] = result
#     # >>> cache[url]
#     # Traceback (most recent call last):
#     #  ...
#     # KeyError: 'http://example.webscraping.com has expired'
#     # >>> cache.clear()
#     def __init__(self, cache_dir='cache', expires=timedelta(seconds=5), compress=True):
#         """
#         cache_dir: the root level folder for the cache
#         expires: timedelta of amount of time before a cache entry is considered expired
#         compress: whether to compress data in the cache
#         """
#         self.cache_dir = cache_dir
#         self.compress = compress
#         self.expires = expires
#
#     def __getitem__(self, url):
#         """Load data from disk for this URL 从磁盘加载此url的数据
#         """
#         path = self.url_to_path(url)
#         if os.path.exists(path):
#             with open(path, 'rb') as fp:
#                 data = fp.read()
#                 if self.compress:
#                     data = zlib.decompress(data)
#                 result, timestamp = pickle.loads(data)
#                 if self.has_expired(timestamp):
#                     raise KeyError(url + ' has expired')
#                 return result
#         else:
#             # URL has not yet been cached
#             raise KeyError(url + ' does not exist')
#
#     def __setitem__(self, url, result):
#         """Save data to disk for this url 向磁盘加载此url的数据
#         """
#         path = self.url_to_path(url)
#         print(path)
#         folder = os.path.dirname(path)
#         if not os.path.exists(folder):
#             os.makedirs(folder)
#         # 转化为字符串
#         data = pickle.dumps((result, datetime.utcnow()))
#         print(data)
#         if self.compress:
#             # 压缩序列化字符串
#             data = zlib.compress(data)
#         with open(path, 'wb') as fp:
#             fp.write(data)
#
#     def __delitem__(self, url):
#         """Remove the value at this key and any empty parent sub-directories
#         """
#         path = self._key_path(url)
#         try:
#             os.remove(path)
#             os.removedirs(os.path.dirname(path))
#         except OSError:
#             pass
#
#     def url_to_path(self, url):
#         """Create file system path fo母不包含’/’，则函数会自动加上r this URL
#         """
#         components = parse.urlsplit(url)
#         # when empty path set to /index.html
#         path = components.path
#         if not path:
#             path = '/index.html'
#         elif path.endswith('/'):
#             path += 'index.html'
#         filename = components.netloc + path + components.query
#         # replace invalid characters
#         filename = re.sub('[^/0-9a-zA-Z\-.,;_ ]', '_', filename)
#         # restrict maximum number of characters
#         filename = '/'.join(segment[:255] for segment in filename.split('/'))
#         return os.path.join(self.cache_dir, filename)
#
#     def has_expired(self, timestamp):
#         """Return whether this timestamp has expired
#         """
#         return datetime.utcnow() > timestamp + self.expires
#
#     def clear(self):
#         """Remove all the cached values
#         """
#         if os.path.exists(self.cache_dir):
#             pass
#             # shutil.rmtree(self.cache_dir)
