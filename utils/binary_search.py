#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/7 14:59
# @Author  : frelikeff
# @Site    : 
# @File    : binary_search.py
# @Software: PyCharm
from typing import List


# 给定一个有序（从小到大）的列表，查找一个给定值,若果存在则返回左边界index，否则返回-1
def binary_search_left(nums: List, target) -> int:
    # 边界条件
    if not len(nums) or target > nums[-1] or target < nums[0]:
        return -1
    # 左右指针
    if target == nums[0]:
        return 0
    if len(nums) == 1:
        return -1

    i, j = 1, len(nums) - 1
    # 开始二分查找
    while i <= j:
        mid = (i + j) // 2
        if nums[mid] < target:
            i = mid + 1
        elif nums[mid] > target:
            j = mid - 1
        else:  # 相等
            if nums[mid] > nums[mid - 1]:
                return mid
            j = mid - 1
    # 查找中无返回那么此时返回-1
    return -1


def binary_search_right(nums: List, target) -> int:
    # 边界条件
    if not len(nums) or target > nums[-1] or target < nums[0]:
        return -1
    if target == nums[-1]:
        return len(nums) - 1
    if len(nums) == 1:
        return -1

    length = len(nums)

    # 左右指针
    i, j = 0, length - 2
    # 开始二分查找
    while i <= j:
        mid = (i + j) // 2
        if nums[mid] < target:
            i = mid + 1
        elif nums[mid] > target:
            j = mid - 1
        else:  # 相等
            if nums[mid] < nums[mid + 1]:
                return mid
            i = mid + 1
    # 查找中无返回那么此时返回-1
    return -1


nums = [5, 7, 7, 8, 8, 10]
target = 8
print(binary_search_right(nums, target))
