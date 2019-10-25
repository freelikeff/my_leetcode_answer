#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/30 15:35
# @Author  : frelikeff
# @Site    : 
# @File    : zero_one_pack.py
# @Software: PyCharm
from typing import List

"""
0,1背包问题，即每件商品只有选和不选两种情况
给出最大收益即可
"""


# 递归，这个递归和下面的非递归其实解决的问题空间是不一样的，至于具体怎么不一样，这里空白不够写不下了。
# 递归的效率可以说是很淡疼了
def ZeroOnePack_dg(things: List[tuple], money) -> int:
    costs = [item[0] for item in things]
    rewards = [item[1] for item in things]
    if len(costs) == 1:
        if money < costs[0]:
            return 0
        else:
            return rewards[0]
    if money >= costs[-1]:
        return max(rewards[-1] + ZeroOnePack_dg(things[:-1], money - costs[-1]),
                   ZeroOnePack_dg(things[:-1], money))
    else:
        return ZeroOnePack_dg(things[:-1], money)


# 非递归，dp
def ZeroOnePack_dp1(things: List[tuple], money: int) -> int:
    memo = [[0 for _ in range(money + 1)] for __ in range(len(things))]  # 商品数n*总资产money+1

    # 由于01背包不需要第一件商品的初始化，他可以自行完成
    for i in range(len(things)):
        for m in range(1, things[i][0]):
            memo[i][m] = memo[i - 1][m]
        for m in range(things[i][0], money + 1):
            # 这里的代码其实有点问题，但是不影响最终结果，因为当i=0时，没有前一行，也就是memo[i-1]越界了，但由于py的特性，表示最后一行，恰好是0
            memo[i][m] = max(things[i][1] + memo[i - 1][m - things[i][0]], memo[i - 1][m])

    return memo[-1][-1]


# dp的空间优化，也没啥说的
def ZeroOnePack_dp2(things: List[tuple], money: int) -> int:
    memo = [0 for _ in range(money + 1)]
    for i in range(len(things)):
        for m in range(money, things[i][0] - 1, -1):  # 这步在不经意间蕴含了一万个细节，好好好看好好学
            memo[m] = max(things[i][1] + memo[m - things[i][0]], memo[m])

    return memo[-1]


if __name__ == '__main__':
    things = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11)]
    answer1 = ZeroOnePack_dg(things, 300)
    answer2 = ZeroOnePack_dp1(things, 300)
    answer3 = ZeroOnePack_dp2(things, 300)
    print(answer1, answer2, answer3)
