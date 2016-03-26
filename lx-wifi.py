#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
import urllib2
import cookielib
import time
import re
print 'Start'
print 'Wait A Moment'


def verify(s_url, s_data, s_header):
    s_request = urllib2.Request(s_url, s_data, s_header)
    s_response = urllib2.urlopen(s_request)
    s_text = s_response.read()
    code = sys.getfilesystemencoding()
    s_text = s_text.decode('utf-8').encode(code)
    s_chick = re.search('zhongyu.', s_text)
    return s_chick


def cookies():
    cj = cookielib.LWPCookieJar()
    cookie_support = urllib2.HTTPCookieProcessor(cj)
    opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
    urllib2.install_opener(opener)


def spider(s_url, s_data, s_headers):
    s_request = urllib2.Request(s_url, s_data, s_headers)
    s_response = urllib2.urlopen(s_request)
    html_content = s_response.read()
    html_code = sys.getfilesystemencoding()
    html_content = html_content.decode('utf-8').encode(html_code)
    return html_content

# get the ip of wireless network adapter
url = "http://sj.dglongxi.com:88/?nasIp=113.98.10.144&nasPortId=DG-WJ-BAS-3.-43001290200000@vlan"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
           'Chrome/90.0.2490.86 Safari/537.36',
           'Referer': 'http://sj.dglongxi.com:88/?nasIp=113.98.10.144&nasPortId=DG-WJ-BAS-3.-43001290200000@vlan'}
text = spider(url, None, headers)
LocalIP = re.search('119.\d+.\d+.\d+', text)
if LocalIP is None:
    print 'Please unplug the network cable and connect to WIFI.'
    raw_input()
    exit()
LocalIP = LocalIP.group()
print LocalIP
# main
HostUrl = 'http://sj.dglongxi.com:88/Weixin.aspx?nasIp=113.98.10.144' \
          '&nasPortId=DG-WJ-BAS-3.-43001290200000%vlan&ip='
HostUrl = HostUrl + LocalIP + '&mac=24%3a0A%3a64%3a8D%3a22%3aEE'
cookies()
postData1 = '__VIEWSTATE=%2FwEPDwULLTE3MTc4Nzg1MTVkZLxUJmMqlxTVnUhDB3tHojLhb%2BRefJw9VlnTgX%2FCERCP&__EVENTVALIDATION=%2FwEWAwLSp5%2FwAQK2xpONDwKBk7XADOgCSeKeqHaTBwbxxCTzUMJZMV%2BambHWgDkAnnKt5a6k&tb_pw=12345&btn_ok=%E8%BF%9E%E6%8E%A5%E4%B8%8A%E7%BD%91'
postData2 = '__VIEWSTATE=%2FwEPDwULLTE3MTc4Nzg1MTVkZLxUJmMqlxTVnUhDB3tHojLhb%2BRefJw9VlnTgX%2FCERCP&__EVENTVALIDATION=%2FwEWAwLSp5%2FwAQK2xpONDwKBk7XADOgCSeKeqHaTBwbxxCTzUMJZMV%2BambHWgDkAnnKt5a6k&tb_pw=02468&btn_ok=%E8%BF%9E%E6%8E%A5%E4%B8%8A%E7%BD%91'
postData3 = '__VIEWSTATE=%2FwEPDwULLTE3MTc4Nzg1MTVkZLxUJmMqlxTVnUhDB3tHojLhb%2BRefJw9VlnTgX%2FCERCP&__EVENTVALIDATION=%2FwEWAwLSp5%2FwAQK2xpONDwKBk7XADOgCSeKeqHaTBwbxxCTzUMJZMV%2BambHWgDkAnnKt5a6k&tb_pw=13579&btn_ok=%E8%BF%9E%E6%8E%A5%E4%B8%8A%E7%BD%91'
postData = postData1
print 'Step 1'
postDataNum = 1
ChickLogin = verify(HostUrl, postData, headers)

while ChickLogin is None:
    postDataNum += 1
    postDataExample = postData + postDataNum
    postData = postDataExample
    print 'Step d%', postDataNum
    ChickLogin = verify(HostUrl, postData, headers)
    if postDataExample == 'postData3':
        print 'Fail to verify.Sorry!'
else:
    print '                      Success!Enjoy the Internet'
    print '                                SoyM                       '
    print '       | | | | | | | | | | | | | | | | | | | | | | | | |   \n\n  ',

    content = raw_input("Please press enter to have the loop or exit.\n")
    if content != "":
        exit()
    else:
        print 'Now we start a loop.You can exit the program to stop..'
        timer = 0
    while True:
        time.sleep(360)
        timer += 1
        request = urllib2.Request(HostUrl, postData, headers)
        response = urllib2.urlopen(request)
        print '\n A loop was finished.Counts=', timer
