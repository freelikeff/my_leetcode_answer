#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/10 12:17
# @Author  : frelikeff
# @Site    : 
# @File    : 52answer.py
# @Software: PyCharm
from typing import List


# 正对角kidx=i+j,反对角tidx=i-j
def helper(n: int, cmemos, kmemos, tmemos, rest: int):
    if rest == 1:
        only_idx = sum(range(n)) - sum(cmemos)
        if only_idx + n - 1 not in kmemos and only_idx - n + 1 not in tmemos:
            return [[only_idx]]
        else:
            return None
    ans = []
    for i in range(n):
        if i not in cmemos and i + n - rest not in kmemos and i - n + rest not in tmemos:
            temp = helper(n, cmemos + [i], kmemos + [i + n - rest], tmemos + [i - n + rest], rest - 1)
            if temp:
                ans.extend([[i] + item for item in temp])
    return ans if ans else None

class Solution:
    def totalNQueens(self, n: int) -> int:
        if n <= 3:
            return 0
        return len(helper(n, [], [], [], n))