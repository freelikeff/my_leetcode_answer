#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/31 15:29
# @Author  : frelikeff
# @Site    : 
# @File    : pack_utils.py
# @Software: PyCharm

from typing import List
from functools import cmp_to_key

"""
这是背包问题一些预处理
"""


@cmp_to_key
def my_cmp(a, b):  # 价格升序，收益降序
    if a[0] == b[0]:
        return b[1] - a[1]
    else:
        return a[0] - b[0]


# 对于完全背包问题
# 如果两件商品AB，cb>=ca,rb<=ra，那么b没有考虑的必要
def diff_costs(things: List[tuple]) -> List[tuple]:  # 传入的数据结构为商品的列表，商品为元组，（cost,reward）
    s_things = sorted(things, key=my_cmp)
    ans = [s_things[0]]

    for item in s_things[1:]:
        if item[1] > ans[-1][1]:
            ans.append(item)

    return ans


def filter_cost_bigger_money(things: List[tuple], money):
    return [item for item in things if item[0] <= money]


if __name__ == '__main__':
    costs = [69, 47, 93, 72, 61, 38, 39, 30, 55, 45]
    rewards = [83, 71, 15, 30, 29, 17, 8, 23, 92, 2]
    things = [(costs[i], rewards[i]) for i in range(len(costs))]
    print(things)
    print(diff_costs(things))
