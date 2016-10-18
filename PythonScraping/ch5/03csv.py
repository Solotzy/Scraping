# coding: utf-8
import os
import csv

directory = "files"
if not os.path.exists(directory):
    os.makedirs(directory)
csvfile = open("files/test.csv", 'w+')
try:
    writer = csv.writer(csvfile)
    writer.writerow(('number','number plus 2', 'number times 2'))
    for i in range(10):
        writer.writerow((i, i+2, i*2))
finally:
    csvfile.close()