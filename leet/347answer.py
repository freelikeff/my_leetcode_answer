#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/9 19:40
# @Author  : frelikeff
# @Site    : 
# @File    : 347answer.py
# @Software: PyCharm
from typing import List
import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        heap = []
        for key, values in c.items():
            if len(heap) < k:
                heapq.heappush(heap, (values, key))
            elif values > heap[0][0]:

                heapq.heappushpop(heap, (values, key))

        return [item[1] for item in heap]