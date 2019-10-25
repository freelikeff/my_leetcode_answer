#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/4 9:24
# @Author  : frelikeff
# @Site    : 
# @File    : 218answer.py
# @Software: PyCharm
from typing import List


# 相当于将xmin到xmax中的所有最高高度存了下来，所以碰到针对性示例，就超时了
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        assert buildings
        xmin = min(buildings, key=lambda item: item[0])[0]
        xmax = max(buildings, key=lambda item: item[1])[1]

        func = dict()
        for left, right, height in buildings:
            for i in range(left, right):
                if func.get(i, 0) < height:
                    func[i] = height

        ans = [[xmin, func[xmin]]]
        base = xmin
        for i in range(xmin, xmax):
            if func.get(i, 0) != func.get(base, 0):
                ans.append([i, func.get(i, 0)])
                base = i

        ans.append([xmax, 0])
        return ans


from heapq import heappush, heappop


class Solution2: #TODO
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = [(L, -H, R) for L, R, H in buildings]
        events += list({(R, 0, 0) for _, R, _ in buildings})
        events.sort()
        print("events",events)

        ans = [[0, 0]]
        heap = [(0, float("inf"))]
        for pos, negH, R in events:
            while heap[0][1] <= pos:
                heappop(heap)
                print(heap)
            if negH:
                heappush(heap, (negH, R))
            if ans[-1][1] != -heap[0][0]:
                ans.append([pos, -heap[0][0]])
        return ans[1:]


if __name__ == '__main__':
    s = Solution2()
    inpt = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
    print(s.getSkyline(inpt))
