# 1.下载zip文件
# 2.从zip中提取csv文件
# 3.解析csv文件
# 4.从中抽取数据
import csv
import io
from zipfile import ZipFile

import chardet
from simple.downloader import Downloader
# /home/amos/下载/top-1m.csv.zip
D=Downloader()
zipped_data=D("http://s3.amazonaws.com/alexa-static/top-1m.csv.zip")

urls=[]
with ZipFile(io.BytesIO(zipped_data)) as zf:
    csv_filename=zf.namelist()[0]
    for _, website in csv.reader(io.StringIO(zf.open(csv_filename).read().decode('utf-8'))):
        urls.append('http://'+website)