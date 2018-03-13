#!/usr/bin/python
# -*- coding: UTF-8 -*-


#定义类
class a():
    #类的成员属性（公共的）
    name = "zhangsan"

    #受保护的（在本类或子类中使用）
    _age = 12

    #私有的（只能在本类中使用）
    __sex = '女'

    #类的方法
    def get(self):
        return self.name

#实例化类
obj = a();
print obj.get()

