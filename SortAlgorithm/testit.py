#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/28 13:08
# @Author  : frelikeff
# @Site    : 
# @File    : testit.py
# @Software: PyCharm


def test_sorted(nums):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True
