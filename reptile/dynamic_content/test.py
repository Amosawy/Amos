
import urllib.request
import urllib.parse

LOGIN_URL='http://example.webscraping.com/usr/login'
LOGIN_EMAIL='amosawy123@163.com'
LOGIN_PASSWORD='ai794613'
data={'email':LOGIN_EMAIL,'password':LOGIN_PASSWORD}
encoded_data=urllib.parse.urlencode(data).encode(encoding='utf-8')
print(encoded_data)
request=urllib.request.Request(LOGIN_URL,encoded_data)
response=urllib.request.urlopen(request)
print(response.geturl())
print(response.code)

print(response.read().decode('utf-8'))


