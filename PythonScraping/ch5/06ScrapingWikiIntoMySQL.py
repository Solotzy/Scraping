# coding: utf8
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random
import pymysql

conn = pymysql.connect(host='192.168.1.190', unix_socket='/tmp/mysql.sock',
                       user='root', passwd=None, db='mysql', charset='utf8')

cur = conn.cursor()
cur.execute("USE scraping")

random.seed(datetime.datetime.now())

# 插入数据
def store(title, content):
    cur.execute("INSERT INTO pages (title, content) VALUES (\"%s\",\"%s\")",
                (title, content))
    cur.connection.commit()

def getLinks(articleUrl):
    html = urlopen("https://zh.wikipedia.org" + articleUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    title = bsObj.find("h1").get_text()
    content = bsObj.find("div",{"id": "mw-content-text"}).find("p").get_text()
    store(title, content)
    return bsObj.find("div", {"id": "bodyContent"}).findAll("a",
                      href=re.compile("^(/wiki/)((?!:).)*$"))
# /wiki/凯文·贝肯
links = getLinks("/wiki/%E5%87%AF%E6%96%87%C2%B7%E8%B4%9D%E8%82%AF")
try:
    count = 1
    while len(links) > 0:
        newArticle = links[random.randint(0, len(links) - 1)].attrs["href"]
        print("抓取了" + str(count) + "条，正在抓取的URL：" + newArticle)
        count += 1
        links = getLinks(newArticle)
finally:
    cur.close()
    conn.close()

