from django.conf import settings
from smtplib import SMTP, SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText

def send(receiver,alert_context):
    # 请自行修改下面的邮件发送者和接收者
    sender = settings.EMAIL_SENDER['addr']  # 发送者的邮箱地址
    receivers = [receiver]  # 接收者的邮箱地址
    message = MIMEText('Alert:'+str(alert_context), _subtype='plain', _charset='utf-8')
    message['From'] = sender #Header(sender, 'utf-8')  # 邮件的发送者
    message['To'] = Header('Hello', 'utf-8')  # 邮件的接收者
    message['Subject'] = Header(alert_context, 'utf-8')  # 邮件的标题
    # smtper = SMTP('smtp.qq.com',465)
    smtper = SMTP_SSL("smtp.qq.com", 465)
    # 请自行修改下面的登录口令

    smtper.login(sender, settings.EMAIL_SENDER['api'])  # QQ邮箱smtp的授权码
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成!')