#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re

res = re.match(r'www', 'www.runoob.com').span()
res1 = re.search(r'w', 'www.runoob.com').group(0)

par = re.compile(r'w')
res2 = par.match('www.baidu.com').group()

pas = re.compile(r'\d+')
res3 = pas.findall('fsdf1fsdfs2sfdds3fsdf4fs8fsdf5')

#切割
res4 = re.split(r'[a-z]','a1b2c3d4')

print "findall",re.findall("[a-z]","12sdfsdf45fsdfer7er78tre7")




print res
print res1
print res2
print res3
print res4

#help(re)
