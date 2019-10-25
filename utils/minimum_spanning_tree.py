#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/21 10:18
# @Author  : frelikeff
# @Site    : 
# @File    : minimum_spanning_tree.py
# @Software: PyCharm
"""
最小生成树
应用于有权无向图，需要找到一个权值和最小的方案，把所有节点都连接起来
生成的必然为有权无环图
由于最小生成树本身是一棵生成树，所以需要时刻满足以下两点：
    生成树中任意顶点之间有且仅有一条通路，也就是说，生成树中不能存在回路；
    对于具有 n 个顶点的连通网，其生成树中只能有 n-1 条边，这 n-1 条边连通着 n 个顶点。
"""

from typing import List


# 克鲁斯卡尔算法:更适合于求边稀疏的网的最小生成树
# 时间复杂度e*lg(e),其实就是排序的复杂度，排完序后直接扫描一遍就好了
def Kruskal(nums: List[tuple], n: int):  # 这次不传入邻接矩阵，传入一个list of tuple,(weight,i,j),顶点要求连续，从0开始
    assert n > 1 and len(
        nums) > n - 2, "The number of points must be more than 1 and the number of edges must be more than n-2"
    # 开辟所需空间
    point2color = {i: i for i in range(n)}  # 表示的是 节点：颜色
    color2points = {i: [i] for i in range(n)}  # 表示的是 颜色：节点列表
    ans = []

    # 对边进行排序
    nums.sort()

    for edge in nums:  # 由小到大扫描边
        weight, i, j = edge
        if point2color[i] != point2color[j]:  # 如果这条边的两条边所属不同的图，也就是还没连起来，那么要将他们连起来
            # 也就是说这条边是所需的
            ans.append(edge)
            # 记录下要被合并的图的颜色
            deljcolor = point2color[j]
            for item in color2points[deljcolor]:
                # 将要被合并的颜色图的所有节点全部改颜色
                point2color[item] = point2color[i]
            # 将这些点全部加入到i的颜色重，于是合并完毕
            color2points[point2color[i]] += color2points[deljcolor]
            # 合并后可删除这个颜色
            del color2points[deljcolor]

    if len(color2points) == 1:  # 说明是连通的
        return ans
    return -1


# prim算法，适合于稠密图
# 因为他是按照顶点来完成的
# 时间复杂度 O(n²)
def Prim(nums: List[List[int]], n: int):  # 这个还是传邻接表好一点,节点个数为n，编号从0开始
    assert n > 1, "The number of points must be more than 1 "
    # 初始的点可以随机选,这里选了0节点
    save = {0}
    rest = set(range(1, n))
    ans = []
    while rest:
        minn = (1 << 15, -1, -1)
        for i in save:
            for j in rest:
                if nums[i][j] < minn[0]:
                    minn = (nums[i][j], i, j)

        if minn[1] == -1:
            return -1
        else:
            save.add(minn[2])
            rest.remove(minn[2])
            ans.append(minn)

    return ans


if __name__ == '__main__':
    inpt = [(6, 0, 1), (1, 0, 2), (5, 0, 3), (5, 1, 2), (5, 2, 3), (3, 1, 4), (6, 2, 4), (6, 4, 5), (4, 2, 5),
            (2, 3, 5)]
    # inpt = [(5, 0, 1), (3, 2, 3), (4, 4, 5)]
    nums = [[1 << 15] * 6 for _ in range(6)]
    for weight, i, j in inpt:
        nums[i][j] = nums[j][i] = weight

    print(Prim(nums, 6))
    print(Kruskal(inpt, 6))
