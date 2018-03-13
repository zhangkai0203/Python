#!/usr/bin/python
# -*- coding: UTF-8 -*-

import hashlib

m = hashlib.md5()
m.update('123456')
print "md5加密",m.hexdigest()
print "md5加密",hashlib.md5("123456").hexdigest()

print "ssh1加密",hashlib.sha1('123456').hexdigest()

print "ssh256加密",hashlib.sha256('123456').hexdigest()

