#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/8 21:29
# @Author  : frelikeff
# @Site    : 
# @File    : 1073answer.py
# @Software: PyCharm
from typing import List


def div(b):  # a为负数 b/(-2),返回（商和余数）
    ans = divmod(b, -2)
    if not ans[1]:
        return ans
    return ans[0] + 1, 1


def tran(inpt: List[int]) -> int:
    ans = 0
    for item in inpt:
        ans *= (-2)
        ans += item
    return ans


class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        value1 = 0
        for item in arr1:
            value1 *= (-2)
            value1 += item
        value2 = 0
        for item in arr2:
            value2 *= (-2)
            value2 += item
        num = value1 + value2
        ans = []
        while num:
            temp = div(num)
            num = temp[0]
            ans.append(temp[1])
        return ans[::-1]



