import smtplib
import email.mime.multipart
import email.mime.text
mail_msg = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.baidu.com">这是一个链接</a></p>
"""

msg = email.mime.multipart.MIMEMultipart()
msg['from'] = 'wow4464@163.com'
msg['to'] = '446488651@qq.com'
msg['subject'] = 'test'
txt = email.mime.text.MIMEText(mail_msg, 'html', 'utf-8')
msg.attach(txt)

smtp = smtplib
smtp = smtplib.SMTP()
smtp.connect('smtp.163.com', '25')
smtp.login('wow4464@163.com', 'xxx')
smtp.sendmail(msg['from'], msg['to'], str(msg))
smtp.quit()
