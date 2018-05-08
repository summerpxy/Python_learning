import smtplib
import sys
from email.mime.text import MIMEText
from email.header import Header


def send_subject_mail(address_from, passwd, address_to):
    smtp_obj = smtplib.SMTP("smtp.126.com", 25)
    echo_message = smtp_obj.ehlo()
    response_ok = echo_message[0]
    if response_ok == 250:
        smtp_obj.starttls()
        smtp_obj.login(address_from, passwd)
        msg = MIMEText('爱调研又有新的的问卷了！！', 'plain', 'utf-8')
        msg['Subject'] = Header("有新的调研可用啦", 'utf-8')
        msg['From'] = address_from
        msg['To'] = address_to
        smtp_obj.sendmail(address_from, address_to, msg.as_string())
        smtp_obj.quit()


if __name__ == "__main__":
    if len(sys.argv) > 3:
        address_from = sys.argv[1]
        passwd = sys.argv[2]
        address_to = sys.argv[3]
        send_subject_mail(address_from, passwd, address_to)
