#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/9 10:35
# @Author  : frelikeff
# @Site    : 
# @File    : 451answer.py
# @Software: PyCharm
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        c=Counter(s)
        ans=""
        for item in sorted(c.keys(),key=lambda x:c[x],reverse=True):
            ans+=item*c[item]
        return ans