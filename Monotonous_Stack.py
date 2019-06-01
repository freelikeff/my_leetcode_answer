#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/25 15:53
# @Author  : frelikeff
# @Site    : https://zhuanlan.zhihu.com/p/26465701
# @File    : Monotonous_Stack.py
# @Software: PyCharm
from typing import List


# 维护一个单调递减栈
def nextExceed(inpt: List[int]) -> List[int]:
    ans = [-1 for _ in range(len(inpt))]
    decreasing_stack = []
    i = 0
    while i < len(ans):
        if not len(decreasing_stack) or inpt[i] < inpt[decreasing_stack[-1]]:
            decreasing_stack.append(i)
            i += 1
        else:
            temp = decreasing_stack.pop()
            ans[temp] = i - temp
            print(temp, ans[temp], i, ans, decreasing_stack)
    return ans


inpt = [5, 3, 1, 2, 4]
print(nextExceed(inpt))
