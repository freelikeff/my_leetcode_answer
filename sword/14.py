#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/8 10:50
# @Author  : frelikeff
# @Site    : 
# @File    : 14.py
# @Software: PyCharm
from typing import List


# in-place,经典解法就不用说了，但是有的地方很淡疼的要求保持奇数内部，偶数内部相对位置不变于是有了下面
class Solution:
    def reOrderArray(self, nums: List[int]) -> None:
        if len(nums) < 2:
            return
        front, end = 0, len(nums) - 1
        while front < end:
            if nums[front] & 1:
                front += 1
            if not nums[end] & 1:
                end -= 1
            if (not nums[front] & 1) and nums[end] & 1:
                nums[front], nums[end] = nums[end], nums[front]
                front += 1
                end -= 1

# 要保持稳定，那就借鉴冒泡排序的思想
class Solution2:
    def reOrderArray(self, nums: List[int]) -> None:
        pass

if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    s.reOrderArray(nums)
    print(nums)
