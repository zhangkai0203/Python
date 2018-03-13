#!/usr/bin/python
# -*- coding: UTF-8 -*-

#兼容性

try:
    f = open("test.txt",'r')
    print f.read();
except Exception as msg:
    print msg
else:
    f.close()
    print "正常"



print sum([1,2,3])


class a(object):

    @staticmethod
    def get():
        print "zhangsan"
a.get()

print all([1,2,3,4])
print all([1,2,3,0])

print '字符串空值',all(['a','b','','c'])

print all([])
print all(())


list = [1,2,3,4]
for i in iter(list):
    print i





























