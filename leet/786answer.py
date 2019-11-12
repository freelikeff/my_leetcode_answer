#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/11 19:40
# @Author  : frelikeff
# @Site    : 
# @File    : 786answer.py
# @Software: PyCharm
from typing import List
import heapq



class Solution:
    def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:
        if K == 1:
            return [A[0], A[-1]]
        length = len(A)
        heap = [(A[0] / A[j], 0, j) for j in range( length)]
        heapq.heapify(heap)
        value, h, w = -1, -1, -1
        for i in range(K):
            print(heap)
            if i == K - 1:
                return [A[k] for k in heapq.heappop(heap)[1:]]
            else:
                value, h, w = heapq.heappop(heap)

                if h < w :
                    heapq.heappush(heap, (A[h + 1] / A[w], h + 1, w))



if __name__ == '__main__':
    s = Solution()
    A = [1, 2, 3, 5]

    K = 5
    print(s.kthSmallestPrimeFraction(A, K))
