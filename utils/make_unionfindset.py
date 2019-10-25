#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/9 13:52
# @Author  : frelikeff
# @Site    : 
# @File    : make_unionfindset.py
# @Software: PyCharm


# 手冲一个并查集
# 这个是为了还能查看每个朋友圈的元素用的，如果只需要知道有几个朋友圈，那么用精简版即可
class UnionFindSet:
    def __init__(self, n):
        # 这样适用于已经对所有元素进行连续编号，0至n-1，如果只有名称的话，用个字典也可以
        # 所有人单线联系，只有一个上线，可以发展很多下线
        self.parent = list(range(n))
        self.forest = {i: [i] for i in range(n)}  # 初始化每个人带一个团队，当然，光杆司令
        self.cou = n

    def get_root(self, item):
        while item != self.parent[item]:
            item = self.parent[item]
        return item

    def union(self, p, q):
        p_root = self.get_root(p)
        q_root = self.get_root(q)
        if p_root != q_root:
            self.parent[q_root] = p_root  # 重新认大哥
            self.forest[p_root] += self.forest[q_root]  # 团队入伙
            self.cou -= 1

    def parade(self):
        return list(self.forest.values())

    def get_count(self):
        return self.cou


class UnionFindSetSimple:
    def __init__(self, n):
        # 这样适用于已经对所有元素进行连续编号，0至n-1，如果只有名称的话，用个字典也可以
        # 所有人单线联系，只有一个上线，可以发展很多下线
        self.parent = list(range(n))
        self.cou = n

    def get_root(self, item):
        while item != self.parent[item]:
            item = self.parent[item]
        return item

    def union(self, p, q):
        p_root = self.get_root(p)
        q_root = self.get_root(q)
        if p_root != q_root:
            self.parent[q_root] = p_root  # 重新认大哥
            self.cou -= 1

    def get_count(self):
        return self.cou
