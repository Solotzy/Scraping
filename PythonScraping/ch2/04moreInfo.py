# coding: utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()

# def getLinks(pageUrl):
#     global pages
#     html = urlopen("http://en.wikipedia.org" + pageUrl)
#     bsObj = BeautifulSoup(html, "html.parser")
#     try:
#         print(bsObj.h1.get_text())
#         print(bsObj.find(id="mw-content-text"))