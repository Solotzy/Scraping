from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO
from bs4 import BeautifulSoup

wordFile = urlopen("http://pythonscraping.com/pages/AWordDocument.docx").read()
# 读成二进制文件对象
wordFile = BytesIO(wordFile)
# 解压缩
document = ZipFile(wordFile)
xml_content = document.read('word/document.xml')
#print(xml_content.decode('utf-8'))

wordObj = BeautifulSoup(xml_content.decode('utf-8'), "html.parser")
textString = wordObj.findAll("w:t")
for textElem in textString:
    closeTag = ""
    try:
        style = textElem.parent.previousSibling.find("w:pstyle")
        if style is not None and style["w:val"] == "Title":
            print("<h1>")
            closeTag = "</h1>"
    except AttributeError:
        # 不打印标签
        pass
        print(textElem.text)
        print(closeTag)
