#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/11 18:55
# @Author  : frelikeff
# @Site    : 
# @File    : 1046answer.py
# @Software: PyCharm
from typing import List
import heapq


# 针对这个特定问题的最大堆版本
class MaxHeap:
    def __init__(self, nums: List[int]):
        self.memo = [-item for item in nums]
        heapq.heapify(self.memo)

    def push(self, item):
        heapq.heappush(self.memo, -item)

    def pop(self):
        return -heapq.heappop(self.memo)

    def __bool__(self):
        return len(self.memo) >= 2

    def getlast(self):
        if not self.memo:
            return 0
        if len(self.memo) == 1:
            return -self.memo[0]


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = MaxHeap(stones)
        while maxheap:
            y = maxheap.pop()
            x = maxheap.pop()
            if y != x:
                maxheap.push(y - x)

        return maxheap.getlast()
