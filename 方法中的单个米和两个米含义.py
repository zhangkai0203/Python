#!/usr/bin/python

# *函数接收参数为元组

 #例如

def myfun(*args): #相当于 def myfun(1,2,3)    ==> args 就相当于（1,2,3）

　　for a in args:

　　　　print(a)

# **表示函数接收参数为一个字典

def myfun(**args) :#相当于 def myfun({a:1,b:2,c:3}) ==>args 就相当于{a:1,b:2,c:3}

　　for k,v in args:

　　　　print(k,":",v)

