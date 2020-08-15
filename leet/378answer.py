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
                if w < width - 1:
                    heapq.heappush(heap, (matrix[h][w + 1], h, w + 1))


def find_k_in_mat(matrix: List[List[int]], k, rowi=True, coli=True):
    """

    :param coli: True means increase
    :param rowi: True means increase
    :param matrix:
    :param k: means the k smallest
    :return: the k smallest
    """
    height, width = len(matrix), len(matrix[0])
    assert height * width >= k
    istart, iend, idelt = 0, height - 1, 1
    jstart, jend, jdelt = 0, width - 1, 1

    if not rowi:
        jstart, jend, jdelt = width - 1, 0, -1
    if not coli:
        istart, iend, idelt = height - 1, 0, -1
    if k == 1:
        return matrix[istart][jstart]
    if k == 2:
        if height == 1:
            return matrix[0][jstart + jdelt]
        elif width == 1:
            return matrix[istart + idelt][0]
        return min(matrix[istart][jstart + jdelt], matrix[istart + idelt][jstart])

    left, right = matrix[istart][jstart], matrix[iend][jend]
    while left < right:
        mid = (left + right) >> 1
        count = 0
        i, j = istart, jend
        while 0 <= i < height and 0 <= j < width:
            if mid >= matrix[i][j]:
                count += abs(j - jstart) + 1
                i += idelt
            else:
                j -= jdelt
        if count >= k:
            right = mid
        elif count < k:
            left = mid + 1

    return left

class Solution2:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return find_k_in_mat(matrix,k)
if __name__ == '__main__':
    matrix = [[1, 5, 9],
              [10, 11, 13],
              [12, 13, 15]]
    k = 8
    s = Solution()
    print(s.kthSmallest(matrix, 5))
