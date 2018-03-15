#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
import requests
import time
import os

i = 0
def get_data(str):
    time.sleep(1)
    for j in range(0,100,10):

        url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word={}pn={}&gsm=3c&ct=&ic=0&lm=-1&width=0&height=0'.format(str.encode('utf-8'),j)
        html = requests.get(url).text

        pic_url = re.findall('"objURL":"(.*?)",', html, re.S)
        for each in pic_url:
            print i
            try:
                pic = requests.get(each, timeout=10)
            except Exception as msg:
                print '【错误】当前图片无法下载'
                continue
            #判断文件是否存在,不存在就创建
            dirname = os.getcwd() + "\images"

            if not os.path.exists(dirname):
                os.mkdir(dirname)

            string = dirname + '\{}.jpg'.format(int(i))

            global i

            fp = open(string, 'wb')
            fp.write(pic.content)
            fp.close()
            i += 1




get_data(u'小黄人')













