import smtplib
from email.mime.text import MIMEText

msg = MIMEText("The body of the email is here")

msg['Subject'] = "An Email Alert"
msg['Form'] = "tianzeyu1992@163.com"
msg['To'] = "498442999@qq.com"

s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()


