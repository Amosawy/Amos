from pymongo import MongoClient


class MongoQueue:
    # states of a download
    OUTSTANDING,PROCESSING,complete=range(3)
    def __init__(self,client=None,timeout=300):
        self.client=MongoClient('localhost',27017)
        self.db=self.client.cache
        self.timeout=timeout