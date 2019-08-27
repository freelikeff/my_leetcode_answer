#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/27 10:22
# @Author  : frelikeff
# @Site    : 
# @File    : random_shuffle.py
# @Software: PyCharm
from typing import List
import random

"""
随机打乱一个数组，要求:n!重可能都会出现并且概率相同。
"""


def RandomShuf(nums: List[int]) -> None:  # 就地打乱
    for i in range(len(nums) - 1):
        idx = random.randint(i)
        nums[i], nums[idx] = nums[idx], nums[i]



