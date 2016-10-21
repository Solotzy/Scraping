# coding: utf-8
import requests

params = {'firstname': 'Tian', 'lastname': 'Zeyu'}
r = requests.post("http://pythonscraping.com/files/processing.php", data=params)
print(r.text)