#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/3 9:17
# @Author  : frelikeff
# @Site    : 
# @File    : 188answer.py
# @Software: PyCharm
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        assert k
        if k >= len(prices) // 2:  # 代表可以交易无穷次
            money = 0
            for i in range(1, len(prices)):
                money += max(0, prices[i] - prices[i - 1])
            return money
        else:  # 有限次
            height = k + 1
            dp = [[0] * 2 for _ in range(height)]

            # 初始化 dp[-1][k][0]  = 0
            # dp[-1][k][1] = -infinity
            # 之后在更新的时候，第一行并不更新
            for k in range(height):
                dp[k][1] = -(1 << 15)

            # 开始dp
            for i in range(len(prices)):
                for k in range(height - 1,0, -1):
                    dp[k][0] = max(dp[k][0], dp[k][1] + prices[i])
                    dp[k][1] = max(dp[k][1], dp[k - 1][0] - prices[i])

            return dp[-1][0]


if __name__ == '__main__':
    s = Solution()
    inpt = 4, [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]
    answer = s.maxProfit(*inpt)
    print(answer)
