import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def send_zip(attachment_path, user_name, mail_user, mail_pass, receiver):
    # 创建邮件对象
    message = MIMEMultipart()
    message['From'] = user_name + '<' + mail_user + '>'
    message['To'] = 'Recv<' + receiver + '>'

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

