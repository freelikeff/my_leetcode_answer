#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/20 10:09
# @Author  : frelikeff
# @Site    : 
# @File    : 528answer.py
# @Software: PyCharm
from typing import List
import random
import bisect


class Solution:
    def __init__(self, w: List[int]):
        self.presum = [0]
        for weight in w:
            self.presum.append(self.presum[-1] + weight)

    def pickIndex(self) -> int:
        summ = random.randint(1, self.presum[-1])
        return bisect.bisect_left(self.presum, summ) - 1
