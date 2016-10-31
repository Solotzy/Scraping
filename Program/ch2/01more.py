#!/usr/bin/env python3
# -*- coding: utf-8 -*-


################################################################################
#
# Copyright (c) 2016 Jurassic.com, Inc. All Rights Reserved
#
################################################################################
"""
This module provide configure file management service in i18n environment.

Authors: tianzeyu(tianzeyu@jurassic.com.cn)
Date:    2016/10/31 10:31:23
"""

def more(text, numlines=15):
    lines = text.splitlines()   # 效果类似split('\n'),只不过不用再末尾加''
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk: print(line)
        if lines and input('More?') not in ['y', 'Y']: break

if __name__ == '__main__':
    import sys                              # 运行时进行此操作，导入时不进行
    more(open(sys.argv[0]).read(), 10)      # 显示命令行里的文件的页面内容