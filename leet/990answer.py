#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/11 18:31
# @Author  : frelikeff
# @Site    : 
# @File    : 990answer.py
# @Software: PyCharm
from typing import List


# 手冲一个并查集
class UnionFindSet:
    def __init__(self, n):
        # 这样适用于已经对所有元素进行连续编号，0至n-1用个字典也可以
        # 所有人单线联系，只有一个上线，可以发展很多下线
        self.parent = list(range(n))
        self.forest = {i: [i] for i in range(n)}  # 初始化每个人带一个团队，当然，光杆司令,刚开始只带自己

    def get_root(self, item):
        while item != self.parent[item]:
            item = self.parent[item]
        return item

    def union(self, p, q):
        if p == q:
            return
        p_root = self.get_root(p)
        q_root = self.get_root(q)
        if p_root != q_root:
            self.parent[q_root] = p_root  # 重新认大哥
            self.forest[p_root] += self.forest[q_root]  # 团队入伙


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        chr2idx = dict()
        equals = [(string[0], string[-1]) for string in equations if string[1] == "="]
        diffs = [(string[0], string[-1]) for string in equations if string[1] == "!"]
        length = 0

        for a, *_, b in equations:
            if a not in chr2idx:
                chr2idx[a] = length
                length += 1
            if b not in chr2idx:
                chr2idx[b] = length
                length += 1

        UFS = UnionFindSet(length)
        for i, j in equals:
            UFS.union(chr2idx[i], chr2idx[j])

        for i, j in diffs:
            if UFS.get_root(chr2idx[i]) == UFS.get_root(chr2idx[j]):
                return False

        return True
