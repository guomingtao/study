import smtplib
from email.mime.text import MIMEText
import argparse
# 引入smtplib和MIMEText
from time import sleep


def sentemail():
    host = 'smtp.163.com'
    # 设置发件服务器地址
    port = 465
    # 设置发件服务器端口号。注意，这里有SSL和非SSL两种形式，现在一般是SSL方式
    sender = 'guomingtao_110@163.com'
    # 设置发件邮箱，一定要自己注册的邮箱
    pwd = 'CIVOVJSXGZRGTHGV'
    # 设置发件邮箱的授权码密码，根据163邮箱提示，登录第三方邮件客户端需要授权码
    receiver = args.to
    # 设置邮件接收人，可以是QQ邮箱
    #body = '<h1>你已成功打卡</h1><p>guomingtao</p>'
    body = args.body
    # 设置邮件正文，这里是支持HTML的
    msg = MIMEText(body, 'html')
    # 设置正文为符合邮件格式的HTML内容
    msg['subject'] = args.subject
    # 设置邮件标题
    msg['from'] = sender
    # 设置发送人
    msg['to'] = receiver
    # 设置接收人
    try:
        s = smtplib.SMTP_SSL(host, port)
        # 注意！如果是使用SSL端口，这里就要改为SMTP_SSL
        s.login(sender, pwd)
        # 登陆邮箱
        s.sendmail(sender, receiver, msg.as_string())
        # 发送邮件！
        print('Done.邮件发送成功')
    except smtplib.SMTPException:
        print('Error.sent email fail')


if __name__ == '__main__':
    paser = argparse.ArgumentParser(description='python3邮件发送脚本')
    paser.add_argument('--to', type=str, default=None, help='收件人邮件地址')
    paser.add_argument('--subject', type=str, default=None, help='邮件主题')
    paser.add_argument('--body', type=str, default=None, help='邮件内容')
    # paser.add_argument()
    args = paser.parse_args()
    #print(args.to)
    #print(args.subject)
    #print(args.body)
    sentemail()