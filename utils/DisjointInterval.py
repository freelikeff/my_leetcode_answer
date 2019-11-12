#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/3 18:22
# @Author  : frelikeff
# @Site    : 
# @File    : DisjointInterval.py
# @Software: PyCharm

# TODO
"""
这个类维护了一个互不相交的区间集，并且有序
"""
import bisect
class DisjointInterval:
    def __init__(self):
        self.points=[] # 0代表左端点，1代表右端点

    def addrange(self,left,right): # 个人习惯，添加双闭区间




    def remove(self,left,right):
