#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/15 14:53
# @Author  : frelikeff
# @Site    : 
# @File    : shortest_path.py
# @Software: PyCharm
from typing import List
from copy import deepcopy
import heapq


# Dijkstra算法，应用条件
# ①有向无向均可，无负权值边
# ②单源最短路径的最快算法
# ③复杂度 O（n²）
def dijkstra(matrix: List[List], start):
    # 开辟所需空间
    length = len(matrix)
    dist = [1 << 15] * length
    path = [-1] * length
    memo = [True] * length  # bool表示剩余否

    # 初始化源点
    dist[start] = 0
    memo[start] = False

    for i, item in enumerate(matrix[start]):
        if item < dist[i]:
            dist[i] = item
            path[i] = start

    while any(memo):
        select = 1 << 15
        node = -1
        for i in range(length):
            if memo[i] and dist[i] <= select:
                node = i
                select = dist[i]

        memo[node] = False
        for i in range(length):
            if memo[i] and dist[i] > select + matrix[node][i]:
                dist[i] = select + matrix[node][i]
                path[i] = node
    return dist


# 任意两点间的最短路径
def floyd(matrix: List[List]):
    dist = deepcopy(matrix)
    length = len(matrix)
    path = [[-1] * length for _ in range(length)]

    for k in range(length):
        for i in range(length):
            for j in range(length):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    path[i][j] = k

    return dist


if __name__ == '__main__':
    from pprint import pprint

    matrix = [[0, 4, 6, 6, 32768, 32768, 32768],
              [32768, 0, 1, 32768, 7, 32768, 32768],
              [32768, 32768, 0, 32768, 6, 4, 32768],
              [32768, 32768, 2, 0, 32768, 5, 32768],
              [32768, 32768, 32768, 32768, 0, 32768, 6],
              [32768, 32768, 32768, 32768, 1, 0, 8],
              [32768, 32768, 32768, 32768, 32768, 32768, 0]]

    for i in range(len(matrix)):
        print(dijkstra(matrix, i))

    pprint(floyd(matrix))
