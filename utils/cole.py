#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/14 10:39
# @Author  : frelikeff
# @Site    : 
# @File    : cole.py
# @Software: PyCharm

from collections import ChainMap


a = {i: i for i in range(4)}
b = {4: 5, 2: 3, 3: 4, }
c = ChainMap(a, b)
print(c)

for item in b.items():
    print(item)

b=c.new_child()
