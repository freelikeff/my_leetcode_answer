#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/24 10:34
# @Author  : frelikeff
# @Site    : 
# @File    : 130answer.py
# @Software: PyCharm
from typing import List


# 经典BFS，也没啥说的
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 处理corner case
        if not board or len(board) == 1 or len(board[0]) < 2:
            return

        height, width = len(board), len(board[0])
        neibours = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        memo = set()

        def BFS(i, j):
            memo.add((i, j))
            for deti, detj in neibours:
                newi, newj = i + deti, j + detj
                if 0 <= newi < height and 0 <= newj < width and board[newi][newj] == "O" and (newi, newj) not in memo:
                    BFS(newi, newj)

        # 上下边界
        for j in range(width):
            if board[0][j] == "O" and (0, j) not in memo:
                BFS(0, j)
            if board[height - 1][j] == "O" and (height - 1, j) not in memo:
                BFS(height - 1, j)

        # 左右边界
        for i in range(1, height - 1):
            if board[i][0] == "O" and (i, 0) not in memo:
                BFS(i, 0)
            if board[i][width - 1] == "O" and (i, width - 1) not in memo:
                BFS(i, width - 1)

        for i in range(height):
            for j in range(width):
                if (i, j) not in memo and board[i][j] == "O":
                    board[i][j] = "X"
        return


if __name__ == '__main__':
    from pprint import pprint

    s = Solution()
    inpt = [['X', 'X', 'X', 'X'],
            ['X', 'O', 'O', 'X'],
            ['X', 'X', 'O', 'X'],
            ['X', 'O', 'X', 'X']]
    s.solve(inpt)
    pprint(inpt)
