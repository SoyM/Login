#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
import urllib2
import cookielib
import time
import re
print 'Start'
print 'Wait A Moment'
#get the ip of wireless network adapter
url = "http://sj.dglongxi.com:88/?nasIp=113.98.10.144&nasPortId=DG-WJ-BAS-3.-43001290200000@vlan"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36',
           'Referer' : 'http://sj.dglongxi.com:88/?nasIp=113.98.10.144&nasPortId=DG-WJ-BAS-3.-43001290200000@vlan'}
request = urllib2.Request(url,headers=headers)
response = urllib2.urlopen(request)
text = response.read().decode('utf-8')
localip = re.search('119.\d+.\d+.\d+',text)
if localip == None:
    print 'Please unplug the network cable and connect to WIFI.\n'
    raw_input()
    exit()
localip = localip.group()
print localip

#login
hosturl = 'http://sj.dglongxi.com:88/Weixin.aspx?nasIp=113.98.10.144' \
          '&nasPortId=DG-WJ-BAS-3.-43001290200000%vlan&ip='
hosturl = hosturl + localip + '&mac=24%3a0A%3a64%3a8D%3a22%3aEE'

cj = cookielib.LWPCookieJar()
cookie_support = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
urllib2.install_opener(opener)

h = urllib2.urlopen(hosturl)
postData = '__VIEWSTATE=%2FwEPDwULLTE3MTc4Nzg1MTVkZPhqpfH1ePGV6GsRes7lryCAzXe54WDNEryIR8ZrnczT&__EVENTVALIDATION=%2FwEWAwKG9NiwAgK2xpONDwKBk7XADOvG3c%2BuSo9%2FqSH9rT1M63AvZZHRO3REc4Upx0WVBCsp&tb_pw=02468&btn_ok=%E8%BF%9E%E6%8E%A5%E4%B8%8A%E7%BD%91'
request = urllib2.Request(hosturl, postData, headers)
response = urllib2.urlopen(request)
text = response.read()
code=sys.getfilesystemencoding()
print code
text = text.decode('utf-8').encode(code)
print text
print '                                SoyM                       '
print '       | | | | | | | | | | | | | | | | | | | | | | | | |   \n\n  ',

content = raw_input("Please press enter to exit or press'n'to have a heartbeat.\n\n\n\n\n\n")
if (content != "n"):
    exit()
else:
    print 'Now we start a heartbeat.'
    timer = 0
while True:
    timer =+1
    request = urllib2.Request(hosturl, postData, headers)
    response = urllib2.urlopen(request)
    print 'A heartbeat was done.'
    time.sleep(120)
