# -*- coding:utf-8 -*-
import requests
import json

# resp = requests.get('http://localhost:9200/tmdb/_analyze' \
#                     '?analyzer=standard&format=yaml',
#                     data="Fire with Fire")

resp = requests.get('http://localhost:9200/tmdb/_analyze' \
                    '?field=title&format=yaml',
                    data="Fire with Fire")
print resp.text