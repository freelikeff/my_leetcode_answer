#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/23 15:19
# @Author  : frelikeff
# @Site    : 
# @File    : 57.2.py
# @Software: PyCharm
from typing import List

"""
输入一个序列的和s，返回这个连续序列的开始值和结束值，所有序列都需要返回
"""


# 书上方法
# 先从1-2开始，
# 如果和比s小，那么需要加元素，所以end+=1，并更新sum
# 如果和比s大，说明需要减元素，所以start+=1，，并更新sum
# 若果等于，则将解添加至ans，并且end+=1，开始下一轮（简单计算可知，start+=2，，并更新sum）
# 应该是线性的，应为每个元素进窗口出窗口一次
def FindContinueSequence(s: int) -> List[List[int]]:
    assert s >= 3
    ans = []
    start, end = 1, 2
    sum = 3

    while end < (s + 3) // 2:
        if sum == s:
            ans.append([start, end])
            start += 2
            end += 1
            sum += end - 2 * start + 3
        elif sum < s:
            end += 1
            sum += end
        elif sum > s:
            sum -= start
            start += 1

    return ans


# 利用等差数列求和公式，算出来首项后判断是否是整数，如果是整数，说明符合要求
def my_FindContinueSequence(s: int) -> List[List[int]]:
    assert s >= 3
    ans = []
    for n in range(2, s):
        first = s / n + (1 - n) / 2
        if abs(int(first))==first:
            ans.append([int(first), n])
    return ans


if __name__ == '__main__':
    ans = my_FindContinueSequence(45) # [[1, 9], [5, 10], [7, 11], [14, 16], [22, 23]]
    print(ans)
