# -*- coding:utf-8 -*-
import requests
import json


def search(query):
  url = 'http://localhost:9200/tmdb/movie/_search'
  httpResp = requests.get(url, data=json.dumps(query))
  searchHits = json.loads(httpResp.text)['hits']
  print "Num\tRelevance Score\t\tMovie Title"
  for idx, hit in enumerate(searchHits['hits']):
    print "%s\t%s\t\t%s" %(idx + 1, hit['_score'], hit['_source']['title'])

usersSearch = 'basketball with cartoon aliens'
query = {
  "query": {
    "multi_match": {
      "query": usersSearch,
      "fields": ["title^10", "overview"]
    }
  }
}

search(query)