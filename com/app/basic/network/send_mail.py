import smtplib
from email.mime.text import MIMEText
from email.header import Header

smtp_obj = smtplib.SMTP("smtp.126.com", 25)
echo_message = smtp_obj.ehlo()
response_ok = echo_message[0]
if response_ok == 250:
    smtp_obj.starttls()
    smtp_obj.login("wx104@126.com", "wx1988104!@#")
    msg = MIMEText('这是一个测试', 'plain', 'utf-8')
    msg['Subject'] = Header("so long to miss you!", 'utf-8')
    msg['From'] = 'wx104@126.com'
    msg['To'] = "43055025@qq.com"
    smtp_obj.sendmail("wx104@126.com", "43055025@qq.com", msg.as_string())
    smtp_obj.quit()
