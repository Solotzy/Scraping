#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
d = dict(name='Bob', age=20, score=88)
# 序列化
# dumps()返回str，内容是标准的Json，注意s
print(json.dumps(d))
strjson = json.dumps(d)
# dump()方法把Json直接写入一个file-like object 注意没有s
with open('json.txt', 'w') as f:
    json.dump(d, f)

# 反序列化
# loads() 从字符串中 注意s
print(json.loads(strjson))
# load()从file-like object中读取字符串 注意没有s
with open('json.txt', 'r') as fr:
    dic = json.load(fr)
print(dic)