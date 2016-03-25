#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
import urllib2
import cookielib
import time
import re
print 'Start'
print 'Wait A Moment'


def verify(HostUrl, postData, headers):
      request = urllib2.Request(HostUrl, postData, headers)
      response = urllib2.urlopen(request)
      text = response.read()
      code = sys.getfilesystemencoding()
      print code
      text = text.decode('utf-8').encode(code)
      ChickLogin = re.search('zhongyu.', text)
      return ChickLogin
# get the ip of wireless network adapter
url = "http://sj.dglongxi.com:88/?nasIp=113.98.10.144&nasPortId=DG-WJ-BAS-3.-43001290200000@vlan"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/46.0.2490.86 Safari/537.36',
           'Referer': 'http://sj.dglongxi.com:88/?nasIp=113.98.10.144&nasPortId=DG-WJ-BAS-3.-43001290200000@vlan'}
request = urllib2.Request(url, headers=headers)
response = urllib2.urlopen(request)
text = response.read().decode('utf-8')
LocalIP = re.search('119.\d+.\d+.\d+', text)
if LocalIP is None:
    print 'Please unplug the network cable and connect to WIFI.\n'
    raw_input()
    exit()
LocalIP = LocalIP.group()
print LocalIP

# login
HostUrl = 'http://sj.dglongxi.com:88/Weixin.aspx?nasIp=113.98.10.144' \
          '&nasPortId=DG-WJ-BAS-3.-43001290200000%vlan&ip='
HostUrl = HostUrl + LocalIP + '&mac=24%3a0A%3a64%3a8D%3a22%3aEE'

cj = cookielib.LWPCookieJar()
cookie_support = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
urllib2.install_opener(opener)

h = urllib2.urlopen(HostUrl)
postData = '__VIEWSTATE=%2FwEPDwULLTE3MTc4Nzg1MTVkZLxUJmMqlxTVnUhDB3tHojLhb%2BRefJw9VlnTgX%2FCERCP&__EVENTVALIDATION=%2FwEWAwLSp5%2FwAQK2xpONDwKBk7XADOgCSeKeqHaTBwbxxCTzUMJZMV%2BambHWgDkAnnKt5a6k&tb_pw=12345&btn_ok=%E8%BF%9E%E6%8E%A5%E4%B8%8A%E7%BD%91'
postData1 = '__VIEWSTATE=%2FwEPDwULLTE3MTc4Nzg1MTVkZLxUJmMqlxTVnUhDB3tHojLhb%2BRefJw9VlnTgX%2FCERCP&__EVENTVALIDATION=%2FwEWAwLSp5%2FwAQK2xpONDwKBk7XADOgCSeKeqHaTBwbxxCTzUMJZMV%2BambHWgDkAnnKt5a6k&tb_pw=02468&btn_ok=%E8%BF%9E%E6%8E%A5%E4%B8%8A%E7%BD%91'
postData2 = '__VIEWSTATE=%2FwEPDwULLTE3MTc4Nzg1MTVkZLxUJmMqlxTVnUhDB3tHojLhb%2BRefJw9VlnTgX%2FCERCP&__EVENTVALIDATION=%2FwEWAwLSp5%2FwAQK2xpONDwKBk7XADOgCSeKeqHaTBwbxxCTzUMJZMV%2BambHWgDkAnnKt5a6k&tb_pw=13579&btn_ok=%E8%BF%9E%E6%8E%A5%E4%B8%8A%E7%BD%91'

request = urllib2.Request(HostUrl, postData, headers)
response = urllib2.urlopen(request)
text = response.read()
code = sys.getfilesystemencoding()
print code
text = text.decode('utf-8').encode(code)
ChickLogin = re.search('zhongyu.', text)
postDataNum = 1
while ChickLogin is None:
    postDataExample = postData + postDataNum
    postData = postDataExample
    postDataNum += 1
    ChickLogin = verify(HostUrl, postData, headers)
    if postDataExample == 'postdata2':
        print 'Fail to verify.Sorry!'
else:
    print 'Success!Enjoy the Internet'
    print '                                SoyM                       '
    print '       | | | | | | | | | | | | | | | | | | | | | | | | |   \n\n  ',

    content = raw_input("Please press enter to have the loop or exit.\n")
    if content != "":
        exit()
    else:
        print 'Now we start a loop.You can exit the program to stop..'
        timer = 0
    while True:
        timer += 1
        request = urllib2.Request(HostUrl, postData, headers)
        response = urllib2.urlopen(request)
        print '\n A loop was finished.Counts=', timer
        time.sleep(360)
