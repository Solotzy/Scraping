# -*- coding:utf-8 -*-

import requests # requests HTTP library
import json # json parsing

def extract():
    f = open('tmdb.json')
    if f:
        return json.loads(f.read())

def reindex(analysisSettings={}, mappingSettings={}, movieDict={}):
    settings = {
        "settings": {
            "number_of_shards": 1,
            "index": {
                "analysis": analysisSettings
            }
        }
    }

    if mappingSettings:
        settings['mappings'] = mappingSettings
    
    resp = requests.delete("http://localhost:9200/tmdb")
    resp = requests.put("http://localhost:9200/tmdb",
                        data = json.dumps(settings))
    
    bulkMovies = ""
    for id, movie in movieDict.iteritems():
        addCmd = {"index": {"_index": "tmdb",
                            "_type": "movie",
                            "_id": movie["id"]}}
        bulkMovies += json.dumps(addCmd) + "\n" + json.dumps(movie) + "\n"
    
    resp = requests.post("http://localhost:9200/_bulk", data=bulkMovies)

mappingSettings = {
    "movie": {
        "properties": {
            "title": {
                "type": "string",
                "analyzer": "english"
            },
            "overview": {
                "type": "string",
                "analyzer": "english"
            }
        }
    }
}
movieDict = extract()
reindex(mappingSettings=mappingSettings,movieDict=movieDict)