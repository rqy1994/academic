# -*- coding: utf-8 -*-
__author__ = 'rqy'

import requests

login_url = 'http://202.118.201.228/academic/j_acegi_security_check'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
    'Host': '202.118.201.228',
    'Referer':'http://202.118.201.228/homepage/index.do',
    'Connection':'keep-alive'
}


s = requests.session()

#download captcha.jepg
img_captcha = s.get('http://202.118.201.228/academic/getCaptcha.do')
f = open('captcha.jpeg','wb')
f.write(img_captcha.content)
f.close()

#login academic system
def loginAS():
    captcha = raw_input('Please input captcha:')
    data = {'j_username':'','j_password':'','j_captcha':captcha,'login':''}
    s.post(url = login_url,data = data)