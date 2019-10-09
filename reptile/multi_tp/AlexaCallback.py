import csv
import io
from zipfile import ZipFile

# 获取需要下载的链接
class AlexaCallback:
    def __init__(self,max_urls=5):
        self.max_urls=max_urls
        self.seed_url="http://s3.amazonaws.com/alexa-static/top-1m.csv.zip"

    def __call__(self,url,html):
        if url==self.seed_url:
            urls=[]
            with ZipFile(io.BytesIO(html)) as zf:
                csv_filename=zf.namelist()[0]
                data = csv.reader(io.StringIO(zf.open(csv_filename).read().decode('utf-8')))
                for _, website in data:
                    urls.append("http://"+website)
                    if len(urls) == self.max_urls:
                        break
            return urls