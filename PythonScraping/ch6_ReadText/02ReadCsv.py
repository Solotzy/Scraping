# coding: utf-8
from urllib.request import urlopen
from io import StringIO
import csv

data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii', 'ignore')
dataFile = StringIO(data)

csvReader = csv.reader(dataFile)

# for row in csvReader:
#     print(row)

# csv.reader返回的csvReader对象是可迭代的，而且由python的列表对象构成
# 所以可以这样写
for row in csvReader:
    print("The album \"" + row[0] + "\" was released in " + str(row[1]))

print("--------------csv.DictReader-----------------")

# csv.DictReader会返回把csv文件每一行转换成Python的字典对象返回，并把字段列表保存在变量dictReader.fieldnames里
# 注意 要第一行是列名
dictReader = csv.DictReader(StringIO(data))
print(dictReader.fieldnames)
for row in dictReader:
    print(row)
