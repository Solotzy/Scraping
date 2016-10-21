#!/usr/bin/env python3
# -*- coding: utf-8 -*=

import os
print(os.name) # nt
#print(os.uname())

# 环境变量
print(os.environ)
path = os.environ.get('PATH').split(';')
print(len(path))
for p in path:
    if 'Python' in p:    # p.find('Python') != -1
        print(p)

# 目录
# 查看当前目录绝对路径
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来：
print(os.path.join('I:\Git\Scraping\LXF', 'testdir'))
# 然后创建一个目录
# os.mkdir(r'I:\Git\Scraping\LXF\testdir')
# 删除一个目录
# os.rmdir(r'I:\Git\Scraping\LXF\testdir')

# 拆分目录，后一部分总是最后级别的目录或文件名
print(os.path.split(r'I:\Git\Scraping\LXF\testdir\file.txt'))

# os.path.splitext可以直接让你得到文件扩展名
print(os.path.splitext(r'I:\Git\Scraping\LXF\testdir\file.txt'))
# 这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作

# 文件操作
# 对文件重命名
# os.rename('test.txt', 'test.py')
# 删掉文件
# os.remove('test.py')

# 但是复制文件的函数居然在os模块中不存在！原因是复制文件并非由操作系统提供的系统调用
# 幸运的是shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充

# 最后看看如何利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录，只需要一行代码：
print([x for x in os.listdir('.') if os.path.isdir(x)])

# 列出所有的.py文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])


