#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/10 9:34
# @Author  : frelikeff
# @Site    : 
# @File    : 1129answer.py
# @Software: PyCharm
from typing import List


class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        # 邻接表，a[i][j]表示从i到j
        red_table = [[0 for _ in range(n)] for __ in range(n)]
        blue_table = [[0 for _ in range(n)] for __ in range(n)]
        for i, j in red_edges:
            red_table[i][j] = 1
        for i, j in blue_edges:
            blue_table[i][j] = 1

        ans = [-1] * n
        ans[0] = 0

        memo = {(0, 1), (0, 0)}

        deque = [(0, 1, 0), (0, 0, 0)]  # True表示接下来走红色，否则走蓝色
        while deque:
            item = deque.pop(0)

            node, flag, level = item
            if flag:
                find = red_table
            else:
                find = blue_table
            flag ^= 1
            for j in range(n):
                if find[node][j] and (j, flag) not in memo:
                    if ans[j] == -1:
                        ans[j] = level + 1
                    memo.add((j, flag))
                    deque.append((j, flag, level + 1))

        return ans


if __name__ == '__main__':
    s = Solution()
    n = 5
    red_edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
    blue_edges = [[1, 2], [2, 3], [3, 1]]
    print(s.shortestAlternatingPaths(n, red_edges, blue_edges))
