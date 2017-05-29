#!/usr/bin/env python
# -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

def mail(user):
    flag = True
    try:
        sender = '786896996@qq.com'
        msg = MIMEText('邮件内容...', 'plain', 'utf-8')
        msg['From'] = formataddr(['肉球', '786896996@qq.com'])
        msg['To'] = formataddr(['肉球', '2816849947@qq.com'])
        msg['Subject'] = '主题是什么'

        server = smtplib.SMTP('smtp.qq.com', 25)
        server.login(sender,'809011lcp')
        server.sendmail(sender,[user,],msg.as_string())
        server.quit()
    except Exception:
        flag = False
    return flag

ret = mail('2816849947@qq.com')
if ret:
    print('成功')
else:
    print('失败')


#http://www.cnblogs.com/xcblogs-python/p/5727238.html

