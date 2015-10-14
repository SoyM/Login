#!/usr/bin/python3
# -*- coding:utf-8 -*-
import urllib.request
import http.cookiejar
import socket
import time
import os
print ('Start')
print ('Wait A Moment')
localip = socket .gethostbyname(socket .gethostname() )
print (localip)
hosturl = 'http://sj.dglongxi.com:88/Weixin.aspx?nasIp=113.98.10.144' \
          '&nasPortId=DG-WJ-BAS-3.-43001290200000%vlan&ip='
hosturl = hosturl + localip + '&mac='

cj = http.cookiejar.LWPCookieJar()
cookie_support = urllib.request.HTTPCookieProcessor(cj)
opener = urllib.request.build_opener(cookie_support, urllib.request.HTTPHandler)
urllib.request.install_opener(opener)



headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1',
           'Referer' : 'http://sj.dglongxi.com:88/?nasIp=113.98.10.144&nasPortId=DG-WJ-BAS-3.-43001290200000@vlan'}


postData = '__VIEWSTATE=%2FwEPDwULLTE3MTc4Nzg1MTVkZCq9h%2BftRRY%2Fu04HpKFIVPCw314wEn0AtpMtlrxX2jVP' \
           '&__VIEWSTATEGENERATOR=79323071' \
           '&__EVENTVALIDATION=%2FwEWAwLwwNWQCAK2xpONDwKBk7XADC4BQdj5QRNnVO46EHLJd' \
           '%2FkvExw%2FAgGgV8RYixzJe6wH&tb_pw=54321&btn_ok=%E8%BF%9E%E6%8E%A5%E4%B8%8A%E7%BD%91'
postData = postData.encode(encoding='UTF-8')

request = urllib.request.Request(hosturl, postData, headers)
print(request )
response = urllib.request.urlopen(hosturl,postData )
text = response.read()
print(text)

return1=os.system('ping longlongjin.com')
if return1:
    print('\n\n\n\n\nERR_INTERNET_DISCONNECTED\n\n\n')
else:
    print('\n\n\n\n\nINTERNET_CONNECTED\n\n\n')

content = input("Please press enter to exit or press'n'to have a heartbeat.\n\n\n\n\n\n")
if (content != "n"):
    exit()
else:
    print ('Now we start a heartbeat.')
    timer = 0
while True:
    if timer == 30:

        break
    timer = timer+1
    request = urllib.request.Request(hosturl, postData, headers)
    response = urllib.request.urlopen(request)
    print ('A heartbeat was done.')
    time.sleep(120)