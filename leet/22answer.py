#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 9:54
# @Author  : frelikeff
# @Site    : 
# @File    : 22answer.py
# @Software: PyCharm
from typing import List


# 这种递归类似于阶乘，重复计算太多
def helper_dg(n, m):  # n,(    m,)

    if n == m:
        return ["(" + item for item in helper_dg(n - 1, m)]
    assert n < m
    if n == 0:
        return [")" * m]
    else:
        return ["(" + item for item in helper_dg(n - 1, m)] + [")" + item for item in helper_dg(n, m - 1)]


# dp,这是时间效率还不错，93%，但是那些神仙是怎么省内存的？
def helper_dp(n):  # n,(    m,)
    dp = [[")" * i] for i in range(0, n + 1)]
    for left in range(1, n + 1):
        for right in range(left, n + 1):
            if right == left:
                dp[right] = ["(" + item for item in dp[right]]
            else:
                dp[right] = ["(" + item for item in dp[right]] + [")" + item for item in dp[right - 1]]
    return dp[-1]


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if not n:
            return []
        return helper_dp(n)


if __name__ == '__main__':
    # from pprint import pprint as print

    s = Solution()
    ans = s.generateParenthesis(11)
    print(len(ans), len(set(ans)))
