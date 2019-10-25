#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/14 13:44
# @Author  : frelikeff
# @Site    : 
# @File    : 407answer.py
# @Software: PyCharm
from typing import List


class MinHeap:  # 子孙<=祖先
    def __init__(self, nums=None):
        self.data = []
        self.end_idx = -1
        if not nums:
            return
        for item in nums:
            self.push(item)
        return

    def push(self, item):
        self.data.append(item)
        self.end_idx += 1
        start = self.end_idx
        while start > 0:
            parent = (start - 1) >> 1
            if self.data[start] < self.data[parent]:
                self.data[start], self.data[parent] = self.data[parent], self.data[start]
                start = parent
            else:
                break
        return

    def pop(self):
        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        self.end_idx -= 1
        start = 0
        while start < (self.end_idx + 1) >> 1:  # 非叶节点才需要调整，到了叶子位置就没必要了
            left = (start << 1) + 1
            right = (start + 1) << 1
            if right > self.end_idx:  # 说明没有右子节点
                if self.data[start] > self.data[self.end_idx]:
                    self.data[start], self.data[self.end_idx] = self.data[self.end_idx], self.data[start]
                break
            else:

                if self.data[right] < self.data[left]:
                    if self.data[start] > self.data[right]:
                        self.data[start], self.data[right] = self.data[right], self.data[start]
                        start = right
                    else:
                        break
                else:
                    if self.data[start] > self.data[left]:
                        self.data[start], self.data[left] = self.data[left], self.data[start]
                        start = left
                    else:
                        break
        return self.data.pop()

    def __bool__(self):
        return not self.end_idx == -1


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if len(heightMap) < 2 or len(heightMap[0]) < 2:
            return 0
        height, width = len(heightMap), len(heightMap[0])
        rest = [[True for _ in range(width)] for _ in range(height)]  # 记录是否访问过
        heap = MinHeap()
        ans = 0
        # 将边界放入最小堆，携带坐标信息
        for h in range(height):
            for w in range(width):
                if h == 0 or h == height - 1 or w == 0 or w == width - 1:
                    heap.push((heightMap[h][w], h, w))
                    rest[h][w] = False

        surrounding = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上下左右
        # 伪BFS
        while heap:
            value, h, w = heap.pop()
            for delth, deltw in surrounding:
                new_h = h + delth
                new_w = w + deltw
                if -1 < new_h < height and -1 < new_w < width and rest[new_h][new_w]:  # 如果没有越界并且没有访问过，那么访问
                    # 这个柱子上的水量，如果比进入点低，那么就是差值，否则就是0
                    ans += max(0, value - heightMap[new_h][new_w])
                    # 将这个柱子进入堆，他的高度已经变成加了水之后了（即可以给他的周围做挡板）
                    heap.push((max(value, heightMap[new_h][new_w]), new_h, new_w))
                    # 记录已访问
                    rest[new_h][new_w] = False
        return ans


# 别人的代码，参考了下
class Solution2:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        import heapq
        m, n = len(heightMap), len(heightMap[0])
        heap = []
        visited = [[0] * n for _ in range(m)]

        # Push all the block on the border into heap
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = 1

        result = 0
        while heap:
            height, i, j = heapq.heappop(heap)
            for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    result += max(0, height - heightMap[x][y])
                    heapq.heappush(heap, (max(heightMap[x][y], height), x, y))
                    visited[x][y] = 1
        return result


if __name__ == '__main__':
    heightMap = [
        [1, 4, 3, 1, 3, 2],
        [3, 2, 1, 3, 2, 4],
        [2, 3, 3, 2, 3, 1]
    ]
    solu = Solution()
    print(solu.trapRainWater(heightMap))
