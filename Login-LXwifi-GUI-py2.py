#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import Tkinter as tk
import urllib2
import cookielib
import os
from Tkinter import *
import tkMessageBox
import re

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack(pady=50, padx=180)
        self.createWidgets()

    def createWidgets(self):

        self.LABLE = Label(root,text="Made by SoyM" )

        self.LABLE.pack(side='bottom')

        self.LOGIN = tk.Button(self,text="Login",)
        self.LOGIN.pack(pady=10)
        self.LOGIN["command"] = self.login

        self.QUIT = tk.Button(self, text="QUIT", bg='red', command=root.destroy)
        self.QUIT.pack()



    def login(self):

        print ('Start')
        print ('Wait A Moment')
        url = "http://sj.dglongxi.com:88/?nasIp=113.98.10.144&nasPortId=DG-WJ-BAS-3.-43001290200000@vlan"
        headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1',
                   'Referer' : 'http://sj.dglongxi.com:88/?nasIp=113.98.10.144&nasPortId=DG-WJ-BAS-3.-43001290200000@vlan'}
        request = urllib2.Request(url,headers=headers)
        response = urllib2.urlopen(request)
        text = response.read().decode('utf-8')
        localip = re.search('119.\d+.\d+.\d+',text)
        if localip == None:
            tkMessageBox.showerror("Error","Please unplug the network cable and connect to WIFI.")
            exit()
        localip =localip.group(0)
        print localip
        hosturl = 'http://sj.dglongxi.com:88/Weixin.aspx?nasIp=113.98.10.144' \
          '&nasPortId=DG-WJ-BAS-3.-43001290200000%vlan&ip='
        hosturl = hosturl + localip + '&mac='

        cj = cookielib.LWPCookieJar()
        cookie_support = urllib2.HTTPCookieProcessor(cj)
        opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
        urllib2.install_opener(opener)

        postData = '__VIEWSTATE=%2FwEPDwULLTE3MTc4Nzg1MTVkZCq9h%2BftRRY%2Fu04HpKFIVPCw314wEn0AtpMtlrxX2jVP' \
           '&__VIEWSTATEGENERATOR=79323071' \
           '&__EVENTVALIDATION=%2FwEWAwLwwNWQCAK2xpONDwKBk7XADC4BQdj5QRNnVO46EHLJd' \
           '%2FkvExw%2FAgGgV8RYixzJe6wH&tb_pw=54321&btn_ok=%E8%BF%9E%E6%8E%A5%E4%B8%8A%E7%BD%91'
        postData = postData.encode(encoding='UTF-8')

        urllib2.Request(hosturl, postData, headers)
        urllib2.urlopen(hosturl,postData )

        return1=os.system('ping baidu.com')
        if return1:
            print('\n\n\n\n\nERR_INTERNET_DISCONNECTED\n\n\n')
            tkMessageBox.showinfo("NETWORK", "DISCONNECTED")
        else:
            print('\n\n\n\n\nINTERNET_CONNECTED\n\n\n')
            tkMessageBox.showinfo("NETWORK", "Your network is connecting")

root = tk.Tk()
root.title('LX-wifi Login')
app = Application(master=root)
app.mainloop()
