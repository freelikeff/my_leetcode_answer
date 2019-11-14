#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/12 19:32
# @Author  : frelikeff
# @Site    : 
# @File    : BinaryMatrix.py
# @Software: PyCharm
from typing import List


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


if __name__ == '__main__':
    matrix = [[15, 13, 12],
              [13, 11, 10],
              [9, 5, 1]]
    for i in range(1, 10):
        print(find_k_in_mat(matrix, i, rowi=False, coli=False))
