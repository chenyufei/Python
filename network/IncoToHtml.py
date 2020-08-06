"""
在HTML文本中添加图片
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 第三方SMTP服务
mail_host = "smtp.163.com"  # 设置服务器
# 自己的邮箱，通过QQ邮箱设置获取口令
mail_user = "chenyufei20@163.com"  # 用户名
mail_pass = "chenyufei1985"  # 口令

sender = 'chenyufei20@163.com'
receivers = ['251813306@qq.com']  # 接受者的邮箱

# 创建一个带附件的实例
message = MIMEMultipart('related')
message['From'] = Header("发送邮件者Clarence", 'utf-8')
message['To'] = Header("xxxxxxxxxxxxxxxxx@qq.com", 'utf-8')
subject = 'Python SMTP  邮件测试'
message['Subject'] = Header(subject, 'utf-8')

msgAlternative = MIMEMultipart('alternative')
message.attach(msgAlternative)

mail_msg = """
<p>Python 邮件发送测试...</p>
<p><a href="https://deeplearning4j.org/">深度学习java框架链接</a></p>
<p>图片演示: </p>
<p><img src="cid:image1"></p>
"""
msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))
# 指定图片为当前目录下test.png
fp = open('test.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# 定义图片ID， 在HTML文本中引用
msgImage.add_header('Content-ID', '<image1>')
message.attach(msgImage)

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25为SMTP端口号
    smtpObj.login(mail_user, mail_pass)  # 会返回(状态码, "字符串解释")元组信息
    smtpObj.sendmail(sender, receivers, message.as_string())
    print(message)
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
