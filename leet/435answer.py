#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/17 10:44
# @Author  : frelikeff
# @Site    : 452answer,utils.interval_schedule
# @File    : 435answer.py
# @Software: PyCharm
from typing import List


def helper(nums):
    if len(nums) < 2:
        return len(nums)
    arr = sorted(nums, key=lambda x: x[1])

    # 初始化
    cou = 1
    end = arr[0][1]
    for i in range(1, len(arr)):
        if arr[i][0] >= end:
            cou += 1
            end = arr[i][1]
    return cou


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        return len(intervals) - helper(intervals)
