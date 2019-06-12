#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/11 19:17
# @Author  : frelikeff
# @Site    : 
# @File    : 5.py
# @Software: PyCharm
from typing import List


# 这里为了体现算法，稍微做了修改，传入的不是字符串，而是字符列表,
# 字符串由单个空格字符分开，替换成给定字符串
# 就地修改
def replaceSpace(s: List[str], t: str) -> None:
    num = s.count(" ")
    old_length = len(s)
    t_len = len(t)
    s += [0] * num * (t_len - 1)

    i, j = old_length - 1, len(s) - 1
    while i >= 0:
        if s[i] == " ":
            s[j + 1 - t_len:j + 1] = t
            j -= t_len
        else:
            s[j] = s[i]
            j -= 1
        i -= 1


inpt = list("ha ppy new year")
print(inpt)
replaceSpace(inpt, "@#$")
print(inpt)
