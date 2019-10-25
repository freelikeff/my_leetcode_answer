#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/20 14:15
# @Author  : frelikeff
# @Site    : 
# @File    : 329answer.py
# @Software: PyCharm
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        memo = dict()
        process = []
        neibour = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上下左右
        height, width = len(matrix), len(matrix[0])
        for i in range(height):
            for j in range(width):
                process.append((matrix[i][j], i, j))
        process.sort()

        for value, i, j in process:

            maxx = 0
            for di, dj in neibour:
                newi, newj = i + di, j + dj
                if 0 <= newi < height and 0 <= newj < width and matrix[newi][newj] < value:
                    maxx = max(memo.get((newi, newj)), maxx)

            memo[(i, j)] = maxx + 1
        return max(memo.values())


if __name__ == '__main__':
    s = Solution()
    inpt = [
        [9, 9, 4],
        [6, 6, 8],
        [2, 1, 1]
    ]

    answer = s.longestIncreasingPath(inpt)
    print(answer)
