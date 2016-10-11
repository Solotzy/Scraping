# coding: utf-8
from urllib.request import urlopen,urlretrieve
from bs4 import BeautifulSoup

# python 3.x　版本中，urllib.request.urlretrieve可以根据文件的URL下载文件
html = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html, "html.parser")
imageLocation = bsObj.find("a",{"id":"logo"}).find("img")['src']
urlretrieve(imageLocation,"logo.jpg")