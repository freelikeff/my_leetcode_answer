#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/23 16:04
# @Author  : frelikeff
# @Site    : 
# @File    : 137answer.py
# @Software: PyCharm
from typing import List


# 这个方式可以说是很屌了，虽然我没看懂
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a, b = 0, 0
        for item in nums:
            a = (a ^ item) & ~b
            b = (b ^ item) & ~a

        return a


# 剑P279方法,感觉稍微有点问题
class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        pass

if __name__ == '__main__':
    s=Solution()
