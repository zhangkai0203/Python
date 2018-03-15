#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib,urllib2
from bs4 import BeautifulSoup
import time


j = 0

#获取分页数据
def get_url():
    for i in range(1,100):
        url = 'https://www.dbmeinv.com/?pager_offset={}'.format(i)
        get_data(url)
    print "抓取完成"

#获取页面并下载
def get_data(url):

    #下载网页
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    req = urllib2.Request(url,headers=headers)
    res = urllib2.urlopen(req,timeout=10)
    html = res.read()

    #获取url
    soup = BeautifulSoup(html,'html.parser',from_encoding='utf-8')
    list = soup.find_all("img")
    for link in list:
        #下载图片
        global j
        url = link.get('src')
        name = link.get('alt')
        print url
        #time.sleep(1)
        try:
            urllib.urlretrieve(url,'.\images\%s.jpg' %name)
        except Exception as msg:
            print "图片无法写入"
            continue

        j+=1

get_url()

















