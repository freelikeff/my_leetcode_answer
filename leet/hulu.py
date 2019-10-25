#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/6 8:58
# @Author  : frelikeff
# @Site    : 
# @File    : hulu.py
# @Software: PyCharm
from typing import List

# """
# 有 n 个葫芦娃一起玩Hulu杀，他们被分为好人和坏人两个阵营，打乱之后围成一圈，按顺时针序编号为 0 ~ n-1。
# 然后随机选定一个葫芦娃，从他/她开始由 1 到 m 顺时针报数，数到 m 的人被杀，下一个人继续从 1 开始报数，
# 如此循环直到剩下最后一个人，这个人所属阵营获得胜利。我们用一个整型数组 a[i] 表示玩家 i 所属的阵营，
# a[i]=1 表示 i 是好人，a[i]=0 表示 i 是坏人；正整型数组 w[i] 表示玩家 i 被选为起始位置的权重，
# 即玩家 i 有 w[i]/sum(w[i]) 的概率做起始位置。求好人获胜的概率，四舍五入到小数点后五位数字（不足五位需要补零）。
#
# input
# 第一行为 2 个空格分开的整数，分别表示 n 和 m
# 第二行为 n 个空格分开的整数，表示 a[i]
# 第三行为 n 个空格分开的整数，表示 w[i]
# 输入范围 0 < m < n <= 1000，0 < sum(w[i]) <= 10000000
#
# 输出
# 输出一个浮点数，表示好人获胜的概率
# """
#
#
# # 其实就是一个Joseph环的变种
# def helper(length, m):  # 这个函数表示长度为length的数组每m个删除一个，返回最后剩余的idx
#     assert m > 0
#     ans = 0
#     for _ in range(length - 1):
#         ans = (ans + m) % length
#     return ans
#
#
# def pred_man(a: List[bool], w: List[float], m: [int]) -> float:
#     ans = 0
#     first_shoot = helper(len(a), m)
#     for i, item in enumerate(w):
#         if a[(i + first_shoot) % len(a)]:
#             ans += item
#     return ans

"""
Hulu有一些列的视频文件，每个文件都有对应的码率，为整数。输入长度为 n 的视频码率数组 arr ，现在定义两个文件区段之间最大码率为：

            p[i][j] = max(arr[i], arr[i+1], ... , arr[j]), 0 <= i <= j <= n-1.

针对所有满足条件 0 <= i <= j <= n-1 的 (i,j) 对，求 p[i][j] 的总和.

for example
input:n = 3 ;arr = [1,2,2]
output:11
解释：满足要求的 p[0][0] = 1, p[0][1] = 2, p[0][2] = 2, p[1][1] = 2, p[1][2] = 2, p[2][2] = 2.
将这些相加，结果为 11.
"""
def add_all(nums:List[int]):


