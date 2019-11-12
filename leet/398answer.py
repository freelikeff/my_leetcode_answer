#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/3 11:03
# @Author  : frelikeff
# @Site    : 
# @File    : 398answer.py
# @Software: PyCharm
from typing import List
import random


class ReservoirSampling:
    def __init__(self, ):  # 初始化的时候如果池子大小为k，那么必须要先把池子放满传K个值
        self._pool = None

        self._length = 1  # 给新进入流的item准备好的idx

    def additem(self, item):
        if self._pool is None:
            self._pool = item
        else:
            probability = random.random()
            if probability <= 1 / self._length:
                self._pool = item

        self._length += 1

    @property
    def pool(self):
        return self._pool


class Solution:

    def __init__(self, nums: List[int]):
        self.memo = nums

    def pick(self, target: int) -> int:
        RS = ReservoirSampling()
        for idx, item in enumerate(self.memo):
            if item == target:
                RS.additem(idx)

        return RS.pool
