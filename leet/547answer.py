#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/9 14:17
# @Author  : frelikeff
# @Site    : 
# @File    : 547answer.py
# @Software: PyCharm
from typing import List
from utils.make_unionfindset import UnionFindSetSimple


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if len(M) == 1:
            return 1
        ufs = UnionFindSetSimple(len(M))
        for i in range(len(M)):
            for j in range(i + 1, len(M)):
                if M[i][j] == 1:
                    ufs.union(i, j)
        return ufs.cou


# 别人的用dfs写的，也很经典
class Solution2:
    def findCircleNum(self, M: List[List[int]]) -> int:
        visited, ans = set(), 0

        def dfs(i):
            for j in range(len(M[i])):
                if M[i][j] and j not in visited:
                    visited.add(j)
                    dfs(j)

        for i in range(len(M)):
            if i not in visited:
                dfs(i)
                ans += 1
        return ans
