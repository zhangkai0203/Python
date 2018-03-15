#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib2,urllib
from bs4 import BeautifulSoup
import time

k = 0

def get_html(url=''):
    res = urllib2.urlopen(url).read()
    return res


def list_url(html):
    html_doc = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
    list = html_doc.select(".titleInner a")
    for data in list:
        detail_data(get_html(data.get('href')))

def detail_data(html):
    html_doc = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
    list =  html_doc.select(".article-cont img")

    #title =  html_doc.select(".article-cont h1")
    #imgname = title[0].text
    global k

    for i in list:
        link =  i.get("data-echo").split("?url=")
        #urllib.urlretrieve(link[1],u'images\{}{}.jpg'.format(imgname,j))
        #time.sleep(1)
        print k
        try:
            urllib.urlretrieve(link[1], u'images\{}.jpg'.format(k))
        except Exception as msg:
            print "图片无法：",link[1]
            continue

        #print link[1]
        k+=1


def run():

    for n in range(1,10):
        url = "http://www.vccoo.com/a/zxn4r?page={}".format(n)
        list_url(get_html(url))

if __name__ == '__main__':
    run()

