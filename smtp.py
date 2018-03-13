#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host="smtp.163.com"  #设置服务器
mail_user="zhangkai020305@163.com"    #用户名
mail_pass="xiaokai0203"   #口令

#this one is also username too.
sender = 'zhangkai020305@163.com'
# 接收邮件，可设置为你的QQ邮箱或者其他邮箱
receivers = ['13911394670@163.com']


message = MIMEText('This is content of the email', 'plain', 'utf-8')
#this on also must be the sender's address
message['From'] = "zhangkai020305@163.com"
message['To'] =  "my fans"  #receiver's name could be customized

subject = 'Be serious' #title
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print "邮件发送成功"
except smtplib.SMTPException as e:
    print "Error: cannot send my email"
    #print e