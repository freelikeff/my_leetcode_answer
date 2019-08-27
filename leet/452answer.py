#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/17 10:19
# @Author  : frelikeff
# @Site    : 435answer,utils.interval_schedule
# @File    : 452answer.py
# @Software: PyCharm
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) < 2:
            return len(points)
        arr = sorted(points, key=lambda x: x[1])
        cou = 1
        end = arr[0][1]
        for i in range(1, len(arr)):
            if arr[i][0] > end:
                cou += 1
                end = arr[i][1]
        return cou

if __name__ == '__main__':
    nums = [[10, 16], [2, 8], [1, 6], [7, 12]]
    s = Solution()
    print(s.findMinArrowShots(nums))
