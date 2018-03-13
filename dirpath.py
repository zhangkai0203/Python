#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

p = __file__

print "文件的当前目录：" + os.getcwd()

print "文件名称：" + os.path.basename(p)

print "文件的绝对目录：" + p

print "返回路劲名"+os.path.dirname(p)

print "文件是否存在",os.path.exists(p)

print "文件最后访问时间：", os.path.getatime(p)




