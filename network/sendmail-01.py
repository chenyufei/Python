# -*- coding: utf-8 -*-
# @Author: Clarence
# @Date:   2018-09-10 11:25:25
# @Last Modified by:   Clarence
# @Last Modified time: 2018-09-10 16:54:15
"""
如果本机没有sendmail访问，可以使用其他服务商的SMTP访问(QQ、网易、Google等)
一个具体的STMP通信(如发送端邮件服务器与接收端服务器的通信)的过程如下:
1) 发送端邮件服务器(以下简称客户端)与接收端邮件服务器(以下简称服务器)的25号端口建立TCP连接
2) 客户端向服务器发送各种命令，来请求各种服务(如认证、指定发送人和接收人)
3）服务器解析用户的命令，做出相应动作并返回给客户端一个响应。
4) 2)和3)交替进行，知道所有邮件都发送完成或两者的连接被意外中断
"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方SMTP服务
mail_host = "smtp.163.com"  # 设置服务器
# 自己的邮箱，通过QQ邮箱设置获取口令
mail_user = "chenyufei20"  # 用户名
mail_pass = "chenyufei1985"  # 口令

sender = 'chenyufei20@163.com'
receivers = '251813306@qq.com'  # 接受者的邮箱,我的另一个QQ邮箱

'''
如果发送HTML格式的邮件，那么改变MIME类型就可以
发送HTML格式的邮件与发送纯文本消息的邮件不同之处就是将MIMEText中_subtype设置为html
mail_msg = """
<p>Python 邮件发送测试...<p>
<p><a href="http://www.baidu.com">这是一个链接</a></p>
"""
message=MIMEText(mail_msg, 'html', 'utf-8')
'''

# class email.mime.text.MIMEText(_text[, _subtype[, _charset]]) 用于创建主要类型文本的MIME对象，_text是有效负载的字符串,_subtype
# 是次要类型，默认为plain._charset是文本的字符集
message = MIMEText('First Python 邮件发送测试...', 'plain', 'utf-8')
message['from'] = "chenyufei20@163.com"
message['to'] = "251813306@qq.com"

subject = 'First Python SMTP  邮件测试'
message['subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    code, msg = smtpObj.connect(mail_host, port=25)  # 25为SMTP端口号
    print("code=%s,msg=%s" % (code, msg))
    noerror = False
    try:
        print("==========")
        smtpObj.login(mail_user, mail_pass)  # 会返回(状态码, "字符串解释")元组信息
        print("==========")
        noerror = True
    except Exception as e:
        print("===="+e)
    if noerror:
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
except smtplib.SMTPException as e:
    print("Error: 无法发送邮件"+e)

'''
<smtplib.SMTP object at 0x000001ED3DDFCE48>
邮件发送成功
[Finished in 2.9s] 
大家可以在QQ邮箱上设置中账号菜单设置开启STMP服务，然后获得口令，填入mail_pass,这里我就用xxxx表示口令，可以看到邮件发送成功 
注: sender和mail_user要相同，可能QQSTMP服务器需要知道真实的发送者，所以就这样
'''