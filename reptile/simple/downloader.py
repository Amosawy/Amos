import urllib.request as urllib2
class Downloader:
    def __init__(self,user_agent='wswp',cache=None,opener=None):
        self.user_agent=user_agent
        self.cache=cache
        self.opener=opener
    def __call__(self, url):
        result=None
        if self.cache:
            try:
                result=self.cache[url]
                print(result)
            except:
                pass
        if result is None:
            headers={'User-agent':self.user_agent}
            result=self.download(url,headers)
            if self.cache:
                self.cache[url]=result
            print(result)
        return result['html']
    def download(self,url,headers):
        print('downloading', url)
        # 构造一个请求对象
        request = urllib2.Request(url, headers=headers)
        opener=self.opener or urllib2.build_opener()
        response=opener.open(request)
        html=response.read()
        print(html)
        code=response.code
        return {'html':html,'code':code}