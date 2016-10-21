import smtplib
from email.mime.text import MIMEText

mailto_list = ["tianzeyu1992@163.com"]
mail_host = "smtp.qq.com" #设置服务器
mail_port = 465
mail_user = "498442999@qq.com" #用户名
mail_pass = "kqraafsmrcdkcaga" #口令
# kqraafsmrcdkcaga

def send_mail(to_list,sub,content):
    print("Going...")
    me = "田泽玉"+"<"+mail_user+">"
    msg = MIMEText(content,_subtype='plain',_charset='gb2312')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        print("Conn...")
        server = smtplib.SMTP_SSL(mail_host,mail_port)
        #server.connect(mail_host,mail_port)
        print("login...")
        server.login(mail_user,mail_pass)
        print("Sending...")
        server.sendmail(me,to_list,msg.as_string())
        print("Closing...")
        server.close()
        return True
    except Exception as e:
        print(str(e))
        return False

if __name__=='__main__':
    if send_mail(mailto_list,"hello","A eamil from Python"):
        print("发送成功")
    else:
        print("发送失败")
