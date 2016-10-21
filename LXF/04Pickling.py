#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pickle
d = dict(name='Bob', age=20, score=88)
# 序列化
# 把一个对象序列化并写入文件
# pickle.dumps()方法把任意对象序列化成一个bytes 然后，就可以把这个bytes写入文件
print(pickle.dumps(d))  # 注意方法名有s
# 或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like object
with open('dumps.txt', 'wb') as f:
    pickle.dump(d, f)  # 注意方法名没有s

# 反序列化
# 当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象
# 也可以直接用pickle.load()方法从一个file-like object中直接反序列化出对象
with open('dumps.txt', 'rb') as fr:
    dic = pickle.load(fr)
print(dic)

# 当然，这个变量和原来的变量是完全不相干的对象，它们只是内容相同而已。
#
# Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，
# 并且可能不同版本的Python彼此都不兼容，因此，只能用Pickle保存那些不重要的数据，
# 不能成功地反序列化也没关系。

