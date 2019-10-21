import http.cookiejar
import urllib.request
import urllib
import urllib.parse
from io import BytesIO
from pprint import pprint
import lxml.html
from PIL import Image
from lxml import etree
import base64
import pytesseract
from form_login.login import parse_form
def register(email,first_name,last_name,password,password_two,ocr):
    REGISTER_URL="http://example.webscraping.com/places/default/user/register?_next=/places/default/index"
    cj=http.cookiejar.CookieJar()
    opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    html=opener.open(REGISTER_URL).read()
    form=parse_form(html)
    pprint(form)
    form['email']=email
    form['first_name']=first_name
    form['last_name']=last_name
    form['password']=password
    form['password_two']=password_two
    img=extract_image(html.decode('utf-8'))
    captcha=ocr(img)
    form['recaptcha_response_field']=captcha
    pprint(form)
    encode_data=urllib.parse.urlencode(form).encode(encoding='utf-8')
    request=urllib.request.Request(REGISTER_URL,encode_data)
    response=opener.open(request)
    print(response.geturl())
def extract_image(html):
    selector=etree.HTML(html)
    img_data=selector.xpath('//*[@id="recaptcha"]/img/@src')[0]
    # remove data:image/png;base64,
    img_data=img_data.partition(',')[-1]
    img_data=img_data.encode('utf-8')
    # open('test.png','wb').write(base64.b64decode(img_data))
    binary_img_data=base64.b64decode(img_data)
    image=Image.open(BytesIO(binary_img_data))
    return image
def ocr(img):
    # threshold the image to ignore background and keep text
    img.save('captcha_original.png')
    gray = img.convert('L')
    gray.save('captcha_greyscale.png')
    bw = gray.point(lambda x: 0 if x < 1 else 255, '1')
    bw.save('captcha_threshold.png')
    word=pytesseract.image_to_string(bw)
    print(word)
    return word
register('ams111aaa@163.com','aa','aa','ai794613','ai794613',ocr)