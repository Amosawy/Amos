import http.cookiejar
import urllib.request
import urllib.parse
from pprint import pprint

import lxml.html
from lxml import etree

LOGIN_URL='http://example.webscraping.com/places/default/user/login?_next=/places/default/index'
LOGIN_EMAIL='amosawy123@163.com'
LOGIN_PASSWORD='ai794613'
def login_basic():
    # fails because not using formkey
    data={'email':LOGIN_EMAIL,'password':LOGIN_PASSWORD}
    encoded_data=urllib.parse.urlencode(data).encode(encoding='utf-8')
    request=urllib.request.Request(LOGIN_URL,encoded_data)
    response=urllib.request.urlopen(request)
    print(response.geturl())
    print(response.read().decode('utf-8'))
def login_formkey():
    # fails because not using cookies to match formkey
    html=urllib.request.urlopen(LOGIN_URL).read()
    data=parse_form(html)
    data['email']=LOGIN_EMAIL
    data['password']=LOGIN_PASSWORD
    pprint(data)
    encoded_data=urllib.parse.urlencode(data).encode(encoding='utf-8')
    request=urllib.request.Request(LOGIN_URL,encoded_data)
    response=urllib.request.urlopen(request)
    print(response.geturl())
def login_cookies():
    # working login
    cj=http.cookiejar.MozillaCookieJar('cookie.txt')
    opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    html=opener.open(LOGIN_URL).read()
    data=parse_form(html)
    data['email'] = LOGIN_EMAIL
    data['password'] = LOGIN_PASSWORD
    encoded_data=urllib.parse.urlencode(data).encode(encoding='utf-8')
    request=urllib.request.Request(LOGIN_URL,encoded_data)
    response=opener.open(request)
    print(response.geturl())
    cj.save(ignore_discard=True, ignore_expires=True)
    print(cj)
    for item in cj:
        print('Name='+item.name)
        print('Value='+item.value)
    return opener
def login_cookies2():
    cookie=http.cookiejar.MozillaCookieJar('cookie.txt')
    cookie.load('cookie.txt',ignore_discard=True, ignore_expires=True)
    opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
    request=urllib.request.Request(LOGIN_URL)
    response=opener.open(request)
    print(response.geturl())
def parse_form(html):
    tree=lxml.html.fromstring(html)
    data={}
    for e in tree.cssselect('form input'):
        if e.get('name'):
            data[e.get('name')]=e.get('value')
    return data

# login_cookies()
# login_cookies2()
