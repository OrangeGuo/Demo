import smtplib
from email.mime.text import MIMEText
from email.header import Header
from subprocess import check_output


receiver = '1772086465@qq.com'
mail_host = "smtp.qq.com"
mail_user = "1772086465@qq.com"
mail_pass = "mvlngkemdmckdcih"
sender = mail_user
receivers = [receiver]

message = MIMEText("log")
message['From'] = Header(mail_user, 'utf-8')
message['To'] = Header(str(receivers), 'utf-8')
message['Subject'] = Header('my test', 'utf-8')

try:
    mail = smtplib.SMTP_SSL(mail_host, 465)
    mail.login(mail_user, mail_pass)
    mail.sendmail(sender, receivers, message.as_string())
    mail.quit()
    print('邮件发送成功')
except smtplib.SMTPException as e:
    print(e)


