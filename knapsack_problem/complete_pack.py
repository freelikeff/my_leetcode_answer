#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/31 15:16
# @Author  : frelikeff
# @Site    : 
# @File    : complete_pack.py
# @Software: PyCharm
from typing import List
from zero_one_pack import ZeroOnePack_dp2 as zero_one_solve

"""
完全背包问题，也就是说所有商品都是可以无限取（当然由于资产限制也不可能完全无限取）
老规矩还是只得到最优解的数值即可
对于完全背包问题，进行筛选处理可以提高效率（吧），
"""


# 状态转移方程 memo[i][m]=max{memo[i-1][m-k*c] | 0<=k<=money//c,取整}
# 有递归和dp的，具体就不用写了
# 算了还是写一个dp的吧
def CompletePack_dp1(things: List[tuple], money):
    memo = [[0 for _ in range(money + 1)] for __ in range(len(things))]  # 商品数n*总资产money+1

    for i in range(len(things)):
        for m in range(1, things[i][0]):
            memo[i][m] = memo[i - 1][m]
        for m in range(things[i][0], money + 1):
            for the_cost in range(0, m + 1, things[i][0]):
                temp = memo[i - 1][m - the_cost] + (the_cost // things[i][0]) * things[i][1]
                if temp > memo[i][m]:
                    memo[i][m] = temp

    return memo[-1][-1]


# 方法二，转化为01背包问题，然后用01背包问题的方法
def complete2zeroone(things: List[tuple], money, zero_one_solve):
    things_for_01 = []
    for thing in things:
        cost, reward = thing
        while cost <= money:
            things_for_01.append((cost, reward))
            cost *= 2
            reward *= 2

    return zero_one_solve(things_for_01, money)


# 方法三，空间复杂度的优化，时间复杂度也有优化
def CompletePack_dp2(things, money):
    memo = [0 for _ in range(money + 1)]
    for i, thing in enumerate(things):
        for m in range(thing[0], money + 1):
            memo[m] = max(memo[m - thing[0]] + thing[1], memo[m])  # 看似随意的一行代码蕴含了一万个细节
    return memo[-1]


if __name__ == '__main__':
    costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    rewards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    things = [(costs[i], rewards[i]) for i in range(len(costs))]

    answer2 = CompletePack_dp1(things, 300)
    print(answer2)
    answer1 = complete2zeroone(things, 300, zero_one_solve)
    print(answer1)
    answer3 = CompletePack_dp2(things, 300)
    print(answer3)
