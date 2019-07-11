#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/29 18:27
# @Author  : frelikeff
# @Site    : 
# @File    : 46.py
# @Software: PyCharm


# DP
def int_trans_to_str(num: int) -> int:
    assert num >= 0
    if num < 10:
        return 1
    inpt_str = str(num)
    ans = [1] * len(inpt_str)
    if 9 < int(inpt_str[:2]) < 26:
        ans[1] = 2
    for i in range(2, len(ans)):
        k = (9 < int(inpt_str[:2]) < 26)
        if k:
            ans[i] = ans[i - 1] + ans[i - 2]
        else:
            ans[i] = ans[i - 1]
    return ans[-1]
