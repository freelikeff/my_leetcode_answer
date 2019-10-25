#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/3 9:32
# @Author  : frelikeff
# @Site    : 
# @File    : 714answer.py
# @Software: PyCharm
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        today = [0, -prices[0]]  # 用第0天初始化
        for i in range(1, len(prices)):
            today = [max(today[0], today[1] + prices[i] - fee), max(today[1], today[0] - prices[i])]
        return today[0]
