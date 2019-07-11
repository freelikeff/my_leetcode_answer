#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/29 19:01
# @Author  : frelikeff
# @Site    : 
# @File    : 179answer.py
# @Software: PyCharm
from typing import List
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
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

        tran = [str(item) for item in nums]
        tran.sort(key=my_cmp, reverse=True)

        return "".join(tran)


if __name__ == '__main__':
    s = Solution()
    inpt = [1, 2, 3]
    ans = s.largestNumber(inpt)
    print(ans)
