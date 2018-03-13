#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
算术运算符
  +	加 - 两个对象相加	a + b 输出结果 30
  -	减 - 得到负数或是一个数减去另一个数	a - b 输出结果 -10
  *	乘 - 两个数相乘或是返回一个被重复若干次的字符串	a * b 输出结果 200
  /	除 - x除以y	b / a 输出结果 2
  %	取模 - 返回除法的余数	b % a 输出结果 0
  **幂 - 返回x的y次幂	a**b 为10的20次方， 输出结果 100000000000000000000
  //	取整除 - 返回商的整数部分	9//2 输出结果 4 , 9.0//2.0 输出结果 4.0
'''

a = 21
b = 10
c = 0

c = a + b
print "1 - c 的值为：", c

c = a - b
print "2 - c 的值为：", c

c = a * b
print "3 - c 的值为：", c

c = a / b
print "4 - c 的值为：", c

c = a % b
print "5 - c 的值为：", c

# 修改变量 a 、b 、c
a = 2
b = 3
c = a**b
print "6 - c 的值为：", c

a = 10
b = 3
c = a//b
print "7 - c 的值为：", c

'''
Python比较运算符
    ==	等于 - 比较对象是否相等	(a == b) 返回 False。
    !=	不等于 - 比较两个对象是否不相等	(a != b) 返回 true.
    <>	不等于 - 比较两个对象是否不相等	(a <> b) 返回 true。这个运算符类似 != 。
    >	大于 - 返回x是否大于y	(a > b) 返回 False。
    <	小于 - 返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。	(a < b) 返回 true。
    >=	大于等于 - 返回x是否大于等于y。	(a >= b) 返回 False。
    <=	小于等于 - 返回x是否小于等于y。	(a <= b) 返回 true。
'''
a = 21
b = 10
c = 0

if (a == b):
    print "1 - a 等于 b"
else:
    print "1 - a 不等于 b"

if (a != b):
    print "2 - a 不等于 b"
else:
    print "2 - a 等于 b"

if (a <> b):
    print "3 - a 不等于 b"
else:
    print "3 - a 等于 b"

if (a < b):
    print "4 - a 小于 b"
else:
    print "4 - a 大于等于 b"

if (a > b):
    print "5 - a 大于 b"
else:
    print "5 - a 小于等于 b"

# 修改变量 a 和 b 的值
a = 5
b = 20
if (a <= b):
    print "6 - a 小于等于 b"
else:
    print "6 - a 大于  b"

if (b >= a):
    print "7 - b 大于等于 a"
else:
    print "7 - b 小于 a"

'''
Python赋值运算符
    =	简单的赋值运算符	c = a + b 将 a + b 的运算结果赋值为 c
    +=	加法赋值运算符	c += a 等效于 c = c + a
    -=	减法赋值运算符	c -= a 等效于 c = c - a
    *=	乘法赋值运算符	c *= a 等效于 c = c * a
    /=	除法赋值运算符	c /= a 等效于 c = c / a
    %=	取模赋值运算符	c %= a 等效于 c = c % a
    **=	幂赋值运算符	c **= a 等效于 c = c ** a
    //=	取整除赋值运算符	c //= a 等效于 c = c // a
'''
a = 21
b = 10
c = 0

c = a + b
print "1 - c 的值为：", c

c += a
print "2 - c 的值为：", c

c *= a
print "3 - c 的值为：", c

c /= a
print "4 - c 的值为：", c

c = 2
c %= a
print "5 - c 的值为：", c

c **= a
print "6 - c 的值为：", c

c //= a
print "7 - c 的值为：", c

'''
Python逻辑运算符
    and	 x and y	布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。 	(a and b) 返回 20。等同于：&&
    or	x or y	布尔"或" - 如果 x 是非 0，它返回 x 的值，否则它返回 y 的计算值。	(a or b) 返回 10。            等同于：||
    not	 not x	布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	not(a and b) 返回 False 等同于 ！==
'''
a = 10
b = 20

if (a and b):
    print "1 - 变量 a 和 b 都为 true"
else:
    print "1 - 变量 a 和 b 有一个不为 true"

if (a or b):
    print "2 - 变量 a 和 b 都为 true，或其中一个变量为 true"
else:
    print "2 - 变量 a 和 b 都不为 true"

# 修改变量 a 的值
a = 0
if (a and b):
    print "3 - 变量 a 和 b 都为 true"
else:
    print "3 - 变量 a 和 b 有一个不为 true"

if (a or b):
    print "4 - 变量 a 和 b 都为 true，或其中一个变量为 true"
else:
    print "4 - 变量 a 和 b 都不为 true"

if not (a and b):
    print "5 - 变量 a 和 b 都为 false，或其中一个变量为 false"
else:
    print "5 - 变量 a 和 b 都为 true"

'''
Python成员运算符
   in	如果在指定的序列中找到值返回 True，否则返回 False。 	x 在 y 序列中 , 如果 x 在 y 序列中返回 True。
   not in	如果在指定的序列中没有找到值返回 True，否则返回 False。 	x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。
'''

a = 10
b = 20
list = [1, 2, 3, 4, 5];

if (a in list):
    print "1 - 变量 a 在给定的列表中 list 中"
else:
    print "1 - 变量 a 不在给定的列表中 list 中"

if (b not in list):
    print "2 - 变量 b 不在给定的列表中 list 中"
else:
    print "2 - 变量 b 在给定的列表中 list 中"

# 修改变量 a 的值
a = 2
if (a in list):
    print "3 - 变量 a 在给定的列表中 list 中"
else:
    print "3 - 变量 a 不在给定的列表中 list 中"

'''
Python身份运算符
   is	is 是判断两个标识符是不是引用自一个对象	x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False
   is not	is not 是判断两个标识符是不是引用自不同对象	x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。
   
   is 与 == 区别：
   is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
    
'''