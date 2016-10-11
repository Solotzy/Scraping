# coding: utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()

# 递归调用
# python默认的递归限制是1000次
def getLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org" + pageUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # 我们遇到了新页面
                newPage =link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks("")