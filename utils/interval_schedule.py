#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/17 10:03
# @Author  : frelikeff
# @Site    : 
# @File    : interval_schedule.py
# @Software: PyCharm
from typing import List


# 区间调度问题，找出不重复的最多的区间数
# 转化为通俗易懂的现实问题就是，每个区间都是一个会，你最多能参加几个会

def IntervalSchedule(nums: List[List[int]]) -> int:
    if len(nums) < 2:
        return len(nums)
    arr = sorted(nums, key=my_key)

    # 初始化
    cou = 1
    end = arr[0][1]
    for i in range(1, len(arr)):
        if arr[i][0] >= end:
            cou += 1
            end = arr[i][1]
    return cou


def my_key(item):
    return item[1]


if __name__ == '__main__':
    nums = [[10, 16], [2, 8], [1, 6], [7, 12]]
    print(IntervalSchedule(nums))
