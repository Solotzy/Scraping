# -*- coding:utf-8 -*-
import requests
import json

usersSearch = 'basketball with cartoon aliens'
query = {
  "query": {
    "multi_match": {
      "query": usersSearch,
      "fields": ["title^10", "overview"]
    }
  }
}

httpResp = requests.get('http://localhost:9200' +
                        '/tmdb/movie/_validate/query?explain',
                        data = json.dumps(query))
print json.loads(httpResp.text)