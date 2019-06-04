#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/2 20:51
# @Author  : frelikeff
# @Site    : 
# @File    : 54spiral_matrix.py
# @Software: PyCharm

"""
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
示例 2:

输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]
"""
from typing import List


# 自己之前实现的丑陋版，自己已经看不懂了，战胜95%。
# 其实就是一圈一圈来，像大大泡泡糖，每一圈，四个边一个一个来
# 为了避免越界，所以计算了面积，计数达到面积，直接返回ans
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        if matrix:
            height, width = len(matrix), len(matrix[0])
            area = height * width
            ans = []
            cou = 0
            for i in range(height):
                for j in range(i, width - i):
                    ans.append(matrix[i][j])
                    cou += 1
                    if cou == area:
                        return ans
                for jj in range(i + 1, height - i):
                    ans.append(matrix[jj][width - i - 1])
                    cou += 1
                    if cou == area:
                        return ans
                for jjj in range(width - 2 - i, i, -1):
                    ans.append(matrix[height - 1 - i][jjj])
                    cou += 1
                    if cou == area:
                        return ans
                for jjjj in range(height - 1 - i, i, -1):
                    ans.append(matrix[jjjj][i])
                    cou += 1
                    if cou == area:
                        return ans
        else:
            return []


class Solution2:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        ans = []
        while matrix:
            ans.extend(matrix.pop(0))
            next_matrix = []
            # print(matrix)
            for x in zip(*matrix):
                next_matrix.append(x)
            # print(next_matrix)
            matrix = next_matrix[::-1]
        return ans

    def spiralOrder_dg(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        ans = matrix.pop(0)
        next_matrix = []
        for x in zip(*matrix):
            next_matrix.append(list(x))
        # print(next_matrix)

        return ans + self.spiralOrder_dg(next_matrix[::-1])


# 因为列表不支持纵向切片，所以进行数组化
# 即传入的是个二维数组
# 一层一层的扒，递归
class Solution3:
    def spiralOrder_dg(self, matrix):
        """
        :type matrix: np.ndarray
        :rtype: List[int]
        """
        height, width = len(matrix), len(matrix[0])

        if not height or not width:
            return []
        if height == 1:
            return list(matrix[0])
        if width == 1:
            return [hang[0] for hang in matrix]
        ans = list(matrix[0])

        for h in range(1, height - 1):
            ans.append(matrix[h][-1])
        ans.extend(matrix[-1][::-1])

        for h in range(1, height - 1):
            ans.append(matrix[height - h - 1][0])
        return ans + self.spiralOrder_dg(matrix[1:-1, 1:-1])


if __name__ == '__main__':
    import numpy as np

    s = Solution3()
    inpt = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    answer = s.spiralOrder_dg(np.array(inpt))
    print(answer)
