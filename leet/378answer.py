#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/12 13:31
# @Author  : frelikeff
# @Site    : 
# @File    : 378answer.py
# @Software: PyCharm
from typing import List

"""
每行递增
每列递增
找第k小
"""
import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        height, width = len(matrix), len(matrix[0])
        heap = [(matrix[i][0], i, 0) for i in range(height)]
        heapq.heapify(heap)
        value, h, w = -1, -1, -1
        for i in range(k):
            if i == k - 1:
                return heapq.heappop(heap)[0]

            else:
                value, h, w = heapq.heappop(heap)
                if w<width-1:
                    heapq.heappush(heap, (matrix[h][w + 1], h, w + 1))


if __name__ == '__main__':
    matrix = [[1, 5, 9],
              [10, 11, 13],
              [12, 13, 15]]
    k = 8
    s=Solution()
    print(s.kthSmallest(matrix,5))
