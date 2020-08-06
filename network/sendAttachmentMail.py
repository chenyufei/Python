import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 第三方SMTP服务
mail_host = "smtp.163.com"  # 设置服务器
# 自己的邮箱，通过QQ邮箱设置获取口令
mail_user = "chenyufei20"  # 用户名
mail_pass = "chenyufei1985"  # 口令

sender = 'chenyufei20@163.com'
receivers = '251813306@qq.com'  # 接受者的邮箱,我的另一个QQ邮箱

# 创建一个带附件的实例
message = MIMEMultipart()
message['from'] = sender
message['to'] = receivers
subject = 'Python SMTP  邮件测试'
message['Subject'] = Header(subject, 'utf-8')

# 邮件正文内容
message.attach(MIMEText('这是smtp协议发送邮件测试有效负载内容....', 'plain', 'utf-8'))

# 构造附件1，传送当前目录下的test.txt文件，可以看出是直接读取文本二进制流
attr1 = MIMEText(open('client.py', 'rb').read(), 'base64', 'utf-8')
"""
上行代码作用
Content-Type: text/base64; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: base64
"""
attr1["Content_Type"] = 'application/octet-stream'  # 内容是二进制流，不知道文件类型
#
attr1["Content-Disposition"] = 'attachment; filename="send1.txt"'  # Content-Disposition是MIME协议的扩展，支持MIME用户代理如何显示附加的文件
message.attach(attr1)

# 构造附件2，传送当前目录下的test2.txt文件
attr2 = MIMEText(open('server.py', 'rb').read(), 'base64', 'utf-8')
attr2["Content_Type"] = 'application/octet-stream'
attr2['Content-Disposition'] = 'attachment; filename="send2.txt'
message.attach(attr2)

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25为SMTP端口号
    smtpObj.login(mail_user, mail_pass)  # 会返回(状态码, "字符串解释")元组信息
    smtpObj.sendmail(sender, receivers, message.as_string())
    print(message)
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
