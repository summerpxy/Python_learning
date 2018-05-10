#!/usr/bin/python3

import json
import smtplib
from email.header import Header
from email.mime.text import MIMEText
import sys

import requests

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept - Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4882.400 QQBrowser/9.7.13059.400",
    "X-Requested-With": "XMLHttpRequest"
}


def _get_cookie(username, password):
    login_url = "http://www.iclick.cn/iclick/?m=apiuser&a=signIn&username=" + username + "&password=" + password + "&gskey= HTTP/1.1"
    response = requests.get(login_url, headers=headers)
    if response.status_code == requests.codes.ok:
        my_cookie = response.cookies["PHPSESSID"]
        print(my_cookie)
        return my_cookie


def get_data_json(my_cookie):
    api_url = "http://www.iclick.cn/iclick/?m=apisurvey&a=mySurveyList"
    jar = requests.cookies.RequestsCookieJar()
    jar.set("PHPSESSID", my_cookie)
    response = requests.get(api_url, headers=headers, cookies=jar)
    if response.status_code == requests.codes.ok:
        print(response.text)
        my_json = json.loads(response.text)
        response_code = my_json["code"]
        if response_code == 200000:
            return my_json["result"]
        else:
            print("get json failed")


def get_result(json_result):
    need_mail = 0
    for item in json_result:
        is_join = int(item["isjoin"])
        max_count = int(item["maxcount"])
        user_count = item["usercount"]
        if is_join == 0 and user_count < max_count:
            need_mail += 1
    return need_mail


def mail_me(count, from_mail, passwd, to_mail):
    if count == 0:
        return
    else:
        smtp_obj = smtplib.SMTP_SSL("smtp.126.com", 465)
        echo_message = smtp_obj.ehlo()
        response_ok = echo_message[0]
        if response_ok == 250:
            # smtp_obj.starttls()
            smtp_obj.login(from_mail, passwd)
            msg = MIMEText('爱调研又有新的的问卷了！！http://www.iclick.cn/iclick/index.php?m=index&a=index', 'plain', 'utf-8')
            msg['Subject'] = Header("有新的调研可用啦", 'utf-8')
            msg['From'] = from_mail
            msg['To'] = to_mail
            smtp_obj.sendmail(from_mail, to_mail, msg.as_string())
            smtp_obj.quit()


if __name__ == "__main__":
    if len(sys.argv > 5):
        username = sys.argv[1]
        passwd = sys.argv[2]
        from_mail = sys.argv[3]
        password = sys.argv[4]
        to_mail = sys.argv[5]
    mail_me(get_result(get_data_json(_get_cookie(username, passwd))), from_mail, password,
            to_mail)
