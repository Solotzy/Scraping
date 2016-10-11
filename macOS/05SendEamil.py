import smtplib
from email.mime.text import MIMEText

msg = MIMEText("The body of the email is here")

msg['Subject'] = "An Email Alert"
msg['Form'] = "498442999@qq.com"
msg['To'] = "tianzeyu1992@163.com"

s = smtplib.SMTP('smtp.qq.com')
s.send_message(msg)
s.quit()


