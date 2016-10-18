# coding: utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup

# 英文
# textPage = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1.txt")

# 俄文 转换成utf-8
# textPage = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")
# print(textPage.read(), 'utf-8')

# 使用Beautiful
html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html, "html.parser")
content = bsObj.find("div", {"id": "mw-content-text"}).get_text()
print("------------1------------")
print(content)
content = bytes(content, "UTF-8")
print("------------2------------")
print(content)
content = content.decode("UTF-8")
print("------------3------------")
print(content)