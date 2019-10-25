#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/1 19:03
# @Author  : frelikeff
# @Site    : 
# @File    : 785answer.py
# @Software: PyCharm
from typing import List


# BFS，一层一层的flag必须是相反的，如果有节点不满足，那么必不是二部图
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        d = {}

        for i in range(n):
            if i not in d:
                deque = [(i, True)]
                while deque:
                    node, flag = deque.pop(0)
                    for item in graph[node]:
                        if item not in d:
                            d[item] = not flag
                            deque.append((item, not flag))
                        elif d[item] == flag:
                            return False
        return True
