#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/22 10:41
# @Author  : frelikeff
# @Site    : 
# @File    : 973answer.py
# @Software: PyCharm
from typing import List
from heapq import heappush, heapreplace


def n_distance(point):
    return -(point[0] ** 2 + point[1] ** 2)


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for i in range(K):
            heappush(heap, (n_distance(points[i]), i))

        for i in range(K, len(points)):
            n_dis = n_distance(points[i])
            if n_dis > heap[0][0]:
                heapreplace(heap, (n_dis, i))

        return [points[item[1]] for item in heap]


if __name__ == '__main__':
    s = Solution()
    inpt = [[1, 3], [-2, 2]], 1
    print(s.kClosest(*inpt))
