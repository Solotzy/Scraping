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

def store(title, content):
    cur.execute("INSERT INTO pages (title, content) VALUES (\"%s\", \"%s\")", (title, content))
    cur.connection.commit()

def getLinks(articleUrl):
    #     /view/21087.htm
    #
    html = urlopen("http://baike.baidu.com" + articleUrl)
    bsObj = BeautifulSoup(html,"html.parser")
    title = bsObj.find("h1").get_text()
    content = bsObj.find("div", {"class":"lemma-summary"}).find("div").get_text()
    store(title, content)
    return bsObj.find("div", {"class":"main-content"}).findAll("a",
                      href=re.compile("^(/view/)((?!:).)*$"))

links = getLinks("/view/21087")
try:
    while len(links) > 0:
        newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
        print(newArticle)
        links = getLinks(newArticle)
finally:
    cur.close()
    conn.close()