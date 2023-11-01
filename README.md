# Python_web_screenshoot
按照客户要求，此项目的作用是在指定时间内，每隔一定时间访问指定网站并截图。将截图放在指定文件夹中，到达一定数量后压缩为.zip文件并发送给用户邮箱中

技术栈：
1、python + selenium 浏览器操作
2、python + zipfile 文件操作（创建文件、压缩文件夹）
3、smtplib邮箱，邮件发送

此项目使用Edge浏览器驱动（已经一同放在文件中）注意版本
点击Edge浏览器右上角的三点->帮助与反馈->关于Miscroft Edge
<img width="961" alt="1698765585100" src="https://github.com/xiaoxiangyeyuhan/Python_web_screenshoot/assets/101324062/f095e861-52fe-487c-8afe-739375bb2eae">

然后去微软官网寻找对应驱动下载（可能会有些慢，但是在国内相比谷歌会好很多）

代码思路并不复杂，唯一注意点在，2023上半年QQ邮箱进行了一次更新
    message = MIMEMultipart()
    message['From'] = user_name + '<' + mail_user + '>'
    message['To'] = 'Recv<' + receiver + '>'

    subject = 'python邮件发送'
    message['Subject'] = Header(subject, 'utf-8')
对message的格式进行了修改（作者在CSDN与chatgpt上寻找测试代码时发现早些的代码全都报错了）

其次，QQ邮箱/其他邮箱记得开“POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV服务”（在QQ邮箱的设置中）
<img width="602" alt="1698766151470" src="https://github.com/xiaoxiangyeyuhan/Python_web_screenshoot/assets/101324062/97f194d2-acfa-44ce-8ee0-1801799b2fbd">
点击“管理服务”
<img width="617" alt="1698766213773" src="https://github.com/xiaoxiangyeyuhan/Python_web_screenshoot/assets/101324062/bb797bdb-07d4-4126-a97a-b952ec22efae">
点击生成
<img width="630" alt="1698766238567" src="https://github.com/xiaoxiangyeyuhan/Python_web_screenshoot/assets/101324062/e6fc7273-3a91-4984-9607-be11cb0afda0">
这个生成码，可以简单理解为“远程登录的密码”，（不要像我一样，一开始测试的时候一直输QQ密码，结果报错半天，甚至我还去改了好几次QQ邮箱密码）

