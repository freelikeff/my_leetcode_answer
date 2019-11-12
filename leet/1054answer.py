#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/9 19:58
# @Author  : frelikeff
# @Site    : 
# @File    : 1054answer.py
# @Software: PyCharm
from typing import List
import heapq
from collections import Counter


class Solution:
    # TODO 这里有一个间隔插入，很骚的操作
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        counter = dict(Counter(barcodes))
        # 按出现次数统计元素
        sortedCounter = sorted(counter, key=lambda k: 0 - counter[k])
        barcodes = []
        # 重新排序
        for i in sortedCounter:
            barcodes += [i] * counter[i]

        arrangedBarcodes = [0 for _ in range(len(barcodes))]
        # 间隔插入
        arrangedBarcodes[::2] = barcodes[:len(arrangedBarcodes[::2])]
        arrangedBarcodes[1::2] = barcodes[len(arrangedBarcodes[::2]):]

        return arrangedBarcodes
