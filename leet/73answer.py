#!E:\pycharm\my_venv\Scripts\python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/7 10:36
# @Author  : freelikeff
# @Site    : 
# @File    : 73answer.py
# @Software: PyCharm

class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        h, w = len(matrix), len(matrix[0])
        # 记录要清空的行和列
        setrow = set()
        setcol = set()

        # 遍历
        for row in range(h):
            for col in range(w):
                if matrix[row][col] == 0:
                    setrow.add(row)
                    setcol.add(col)

        #清空行
        for find_row in setrow:
            matrix[find_row] = [0] * w

        # 清空列
        for find_col in setcol:
            for item in matrix:
                item[find_col] = 0


if __name__ == "__main__":
    s = Solution()
    inpt = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]
    ans = s.setZeroes(inpt)
    print(inpt)
