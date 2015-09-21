#!/usr/bin/python


import urllib2
import cookielib



hosturl = 'http://sj.dglongxi.com:88/Weixin.aspx?nasIp=113.98.10.144' \
          '&nasPortId=DG-WJ-BAS-3.-43001290200000%vlan&ip=119.144.116.201&mac='


cj = cookielib.LWPCookieJar()
cookie_support = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
urllib2.install_opener(opener)


h = urllib2.urlopen(hosturl)


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1',
           'Referer' : 'http://sj.dglongxi.com:88/Weixin.aspx?nasIp=113.98.10.144&nasPortId=DG-WJ-BAS-3.-43001290200000@vlan&ip=119.141.185.106&mac='}


postData = '__VIEWSTATE=%2FwEPDwULLTE3MTc4Nzg1MTVkZCq9h%2BftRRY%2Fu04HpKFIVPCw314wEn0AtpMtlrxX2jVP&__VIEWSTATEGENERATOR=79323071&__EVENTVALIDATION=%2FwEWAwLwwNWQCAK2xpONDwKBk7XADC4BQdj5QRNnVO46EHLJd%2FkvExw%2FAgGgV8RYixzJe6wH&tb_pw=02468&btn_ok=%E8%BF%9E%E6%8E%A5%E4%B8%8A%E7%BD%91'


request = urllib2.Request(hosturl, postData, headers)
print request
response = urllib2.urlopen(request)
text = response.read()
print text