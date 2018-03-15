#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import re


html = requests.get("http://www.doutula.com/article/list/?page=2").text

list = re.findall(r'data-backup="(.*?)".*?alt="(.*?)"',html,re.S)

for data in list:
    da = u"图片名称：{}》》图片地址：{}".format(data[1],data[0])
    print da
