import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def send_zip(attachment_path):
    # 第三方 SMTP 服务
    user_name = input("请输入您的昵称:")
    mail_user = input("请输入您的QQ邮箱:")  # 用户名
    mail_pass = input("请输入口令:")  # 口令,注意这里的口令是需要到QQ邮箱中开启pop、smtp服务后，qq生成的授权码

    receiver = input("请输入接收者邮箱:")  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    # 创建邮件对象
    message = MIMEMultipart()
    message['From'] = user_name + '<' + mail_user + '>'
    message['To'] = 'Recv' + receiver + ''

    subject = 'python邮件发送'
    message['Subject'] = Header(subject, 'utf-8')

    # 添加附件
    with open(attachment_path, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename="{attachment_path}"')
        message.attach(part)

    try:
        server = smtplib.SMTP_SSL('smtp.qq.com', 465)
        server.login(mail_user, mail_pass)
        print("login成功")
        server.send_message(message)
        print("邮件发送成功")
        server.quit()
    except smtplib.SMTPException as e:
        print(f"Error: 无法发邮件{e}")
