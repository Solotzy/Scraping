# coding: utf-8
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://zh.wikipedia.org/wiki/%E6%96%87%E4%BB%B6%E7%BC%96%E8%BE%91%E5%99%A8%E6%AF%94%E8%BE%83")
bsObj = BeautifulSoup(html, "html.parser")
# 主对比表格是当前页面上的第一个表格
table = bsObj.findAll("table", {"class":"wikitable"})[0]
rows = table.findAll("tr")

csvFile = open("files/editors.csv", 'wt', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()