#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 15:24
# @Author  : frelikeff
# @Site    : 
# @File    : 914answer.py
# @Software: PyCharm
from typing import List
from collections import Counter


# from math import gcd
def gcd(num1, num2):  # a<b
    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return num1


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        cou = sorted(Counter(deck).values())
        if len(cou) == 1 and len(deck) > 1:
            return True
        start = cou[0]
        for item in cou[1:]:
            start = gcd(start, item)
            if start == 1:
                return False
        return True
