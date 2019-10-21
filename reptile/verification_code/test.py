import http.cookiejar
import urllib.request
import urllib
from io import BytesIO
from pprint import pprint
import lxml.html
from PIL import Image
from lxml import etree
import base64

from form_login.login import parse_form
def register():
    REGISTER_URL="http://example.webscraping.com/places/default/user/register"
    cj=http.cookiejar.CookieJar()
    opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    html=opener.open(REGISTER_URL).read()
    form=parse_form(html)
    pprint(form)
    return html
def extract_image(html):
    selector=etree.HTML(html)
    img_data=selector.xpath('//*[@id="recaptcha"]/img/@src')[0]
    # remove data:image/png;base64,
    img_data=img_data.partition(',')[-1]
    img_data=img_data.encode('utf-8')
    # open('test.png','wb').write(base64.b64decode(img_data))
    binary_img_data=base64.b64decode(img_data)
    image=Image.open(BytesIO(binary_img_data))
    # image.save('test.png')
    # tree=lxml.html.fromstring(html)
    # img_data=tree.cssselect('div#recaptcha img')[0].get('src')
    # print(img_data)
html=register()
extract_image(html.decode('utf-8'))