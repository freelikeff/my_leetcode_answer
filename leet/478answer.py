#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/21 16:35
# @Author  : frelikeff
# @Site    : 
# @File    : 478answer.py
# @Software: PyCharm
from typing import List
from random import random


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.x = x_center
        self.y = y_center
        self.xmin = x_center - radius
        self.ymin = y_center - radius
        self.r2 = 2 * radius
        self.rr = radius ** 2

    def randPoint(self) -> List[float]:
        x = random() * self.r2 + self.xmin
        y = random() * self.r2 + self.ymin
        if self.incircle(x, y):
            return [x, y]
        return self.randPoint()

    def incircle(self, x, y):
        return (x - self.x) ** 2 + (y - self.y) ** 2 <= self.rr
