#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/29 18:48
# @Author  : frelikeff
# @Site    : 179answer
# @File    : 45.py
# @Software: PyCharm
from typing import List
from functools import cmp_to_key


def find_min_number(nums: List[int]) -> str:
    if not nums or not any(nums):
        return "0"

    @cmp_to_key
    def my_cmp(a: str, b: str):
        if a + b < b + a:
            return -1
        elif a + b > b + a:
            return 1
        else:
            return 0

    tran = [str(item) for item in nums if item > 0]
    tran.sort(key=my_cmp)

    return "".join(tran)


if __name__ == '__main__':
    inpt = [0, 0, 0, 50, 1]
    ans = find_min_number(inpt)
    print(ans)
