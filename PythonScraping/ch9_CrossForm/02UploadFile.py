import requests

file = {'uploadFile': open('file/Build.png', 'rb')}
r = requests.post("http://pythonscraping.com/pages/processing2.php", files=file)
print(r.text)