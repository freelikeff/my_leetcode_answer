#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/30 18:35
# @Author  : frelikeff
# @Site    : 
# @File    : 327answer.py
# @Software: PyCharm
from typing import List
import bisect


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        p = [0]  # 前缀和初始化，前缀和p[x]，就是区间数组[0, x)的和
        for i in nums:
            p += [p[-1] + i]  # 前缀和计算
        ans = 0
        q = []  # 有序的前缀和队列
        for pi in p[:: -1]:  # 逆序遍历前缀和
            i, j = pi + lower, pi + upper  # 给出当前前缀和两个对应边界
            l = bisect.bisect_left(q, i)  # 二分查找
            r = bisect.bisect_right(q, j)  # 找到对应边界的在前缀和数组里的插入位置
            ans += r - l  # 序号大于自己的前缀和里有多少个前缀和在边界里面，就是以当前区间为起点，符合区间和条件的个数
            bisect.insort(q, pi)  # 二分插入更新队列
        return ans


if __name__ == '__main__':
    s = Solution()
    inpt = [-2, 5, -1], -2, 2
    print(s.countRangeSum(*inpt))
