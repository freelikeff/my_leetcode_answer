#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/3 8:55
# @Author  : frelikeff
# @Site    : 
# @File    : 309answer.py
# @Software: PyCharm
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 因为交易次数限制为正无穷，所以k的情况等于k-1
        thedaybeforeyester = [0, -prices[0]]  # 用第0天初始化
        yesterday = [max(0, prices[1] - prices[0]), max(-prices[0], -prices[1])]
        for i in range(2, len(prices)):
            today = [max(yesterday[0], yesterday[1] + prices[i]), max(yesterday[1], thedaybeforeyester[0] - prices[i])]
            thedaybeforeyester, yesterday = yesterday, today

        return yesterday[0]


if __name__ == '__main__':
    s = Solution()
    inpt = [1, 2]
    print(s.maxProfit(inpt))
