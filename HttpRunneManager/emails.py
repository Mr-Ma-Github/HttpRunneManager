import io
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import os

from HttpRunnerManager.settings import EMAIL_SEND_USERNAME, EMAIL_SEND_PASSWORD, EMAIL_HOST, EMAIL_PORT
# EMAIL_SEND_USERNAME = '283340479@qq.com'  # 定时任务报告发送邮箱，支持163,qq,sina,企业qq邮箱等，注意需要开通smtp服务
# EMAIL_SEND_PASSWORD = '*************'     # qq邮箱授权密码


def send_email_reports(receiver, html_report_path):
    if '@sina.com' in EMAIL_SEND_USERNAME:
        smtp_server = 'smtp.sina.com'
    elif '@163.com' in EMAIL_SEND_USERNAME:
        smtp_server = 'smtp.163.com'
    elif '@qq.com' in EMAIL_SEND_USERNAME:
        smtp_server = 'smtp.qq.com'
    else:
        smtp_server = EMAIL_HOST

    subject = "接口自动化测试报告"

    with io.open(html_report_path, 'r', encoding='utf-8') as stream:
        send_file = stream.read()

    att = MIMEText(send_file, "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = "attachment;filename = TestReports.html"

    body = MIMEText("附件为定时任务生成的接口测试报告，请查收，谢谢！", _subtype='html', _charset='gb2312')

    msg = MIMEMultipart('related')
    msg['Subject'] = subject
    msg['from'] = EMAIL_SEND_USERNAME
    msg['to'] = receiver
    msg.attach(att)
    msg.attach(body)

    # smtp = smtplib.SMTP(port=EMAIL_PORT)
    # smtp.connect(smtp_server, port=EMAIL_PORT)
    # smtp.starttls()
    # smtp.login(EMAIL_SEND_USERNAME, EMAIL_SEND_PASSWORD)
    #
    #
    # smtp.sendmail(EMAIL_SEND_USERNAME, receiver.split(','), msg.as_string())
    # smtp.quit()

    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtp_server)                      # 连服务器
        smtp.login(EMAIL_SEND_USERNAME, EMAIL_SEND_PASSWORD)
    except:
        smtp = smtplib.SMTP_SSL(smtp_server, EMAIL_PORT)
        smtp.login(EMAIL_SEND_USERNAME, EMAIL_SEND_PASSWORD)                       # 登录
    smtp.sendmail(EMAIL_SEND_USERNAME, receiver.split(','), msg.as_string())
    smtp.quit()


if __name__ == '__main__':
    send_email_reports('283340479@qq.com', 'D:\\soft\\2020.html')
