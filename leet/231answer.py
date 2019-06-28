#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/29 15:45
# @Author  : frelikeff
# @Site    : 
# @File    : 231answer.py
# @Software: PyCharm
"""
给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

示例 1:

输入: 1
输出: true
解释: 20 = 1
示例 2:

输入: 16
输出: true
解释: 24 = 16
示例 3:

输入: 218
输出: false
"""


# 关键点：一个数和与它小1的数做位与，即n&(n-1)
# 结果是将二进制的n最右的1变为0，其他位不变
# 对于2的幂来说，只有最左是1，所以做如上操作后应该变为全0，即0
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0
