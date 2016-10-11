#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# g保存的是算法 每次调用next(g)，就计算出下一个元素
# 直到计算到最后一个元素，没有更多的元素的时候，抛出StopIteration的错误
g = (x * x for x in range(10))
for n in g:
    print(n)


