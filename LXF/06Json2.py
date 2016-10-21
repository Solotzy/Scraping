#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

class Student(object):
    def __init__(self, name, age, score):
        '''

        :param name: str
        :param age: int
        :param score: float
        '''
        self.name = name
        self.age = age
        self.score = score

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

s = Student('Bob', 20, 88)
# 序列化
# 这样，Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON
print(json.dumps(s, default=student2dict))

# 不过，下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict：
print(json.dumps(s, default=lambda obj: obj.__dict__))
# 因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。

# 反序列化
# 同样的道理，如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，
# 然后，我们传入的object_hook函数负责把dict转换为Student实例：
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

stu = json.dumps(s, default=lambda obj: obj.__dict__)
print(json.loads(stu, object_hook=dict2student))

