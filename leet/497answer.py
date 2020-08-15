#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/22 9:46
# @Author  : frelikeff
# @Site    : 
# @File    : 497answer.py
# @Software: PyCharm
from typing import List
from random import randint
import bisect


class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.presum = [0]
        for x1, y1, x2, y2 in rects:
            self.presum.append(self.presum[-1] + (x1 - x2-1) * (y1 - y2-1))

    def pick(self) -> List[int]:
        idx = bisect.bisect_left(self.presum, randint(1, self.presum[-1]))  # 先选择哪个矩形
        return [randint(self.rects[idx][0],self.rects[idx][2]),randint(self.rects[idx][1],self.rects[idx][3])]

