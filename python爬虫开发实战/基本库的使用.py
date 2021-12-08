#-*- coding:utf-8 -*-
#登录验证
from urllib.request import HTTPPasswordMgrWithDefaultRealm,HTTPBasicAuthHandler,build_opener
from urllib.error import URLError
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

username = 'admin'
password = 'admin'
url = 'https://ssr3.scrape.center/'

p = HTTPPasswordMgrWithDefaultRealm()

p.add_password(None,url,username,password)

auth_handler = HTTPBasicAuthHandler(p)

opener = build_opener(auth_handler)
try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)
    
####################百度cookie获取#############
import http.cookiejar,urllib.request

cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.baidu.com')
for item in cookie:
    print(item.name + '=' + item.value)
    
    
    
#
