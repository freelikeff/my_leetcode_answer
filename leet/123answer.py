#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/2 8:40
# @Author  : frelikeff
# @Site    : 
# @File    : 123answer.py
# @Software: PyCharm
from typing import List


# 状态机，唉，最近越来越懒得写注释了，感觉没什么心劲
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        height = 3  # 表示最大交易次数为2次
        dp = [[0] * 2 for _ in range(height)]

        # 初始化 dp[-1][k][0]  = 0
        # dp[-1][k][1] = -infinity
        # 之后在更新的时候，第一行并不更新
        for k in range(height):
            dp[k][1] = -(1 << 15)

        # 开始dp
        for i in range(len(prices)):
            for k in range(height-1,0,-1):

                dp[k][0] = max(dp[k][0], dp[k][1] + prices[i])
                dp[k][1] = max(dp[k][1], dp[k-1][0] - prices[i])

        return dp[-1][0]


if __name__ == '__main__':
    s = Solution()
    inpt = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]
    print(s.maxProfit(inpt))
