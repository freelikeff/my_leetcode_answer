#!E:\pycharm\my_venv\Scripts\python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/13 21:49
# @Author  : freelikeff
# @Site    : 
# @File    : 152answer.py
# @Software: PyCharm

from operator import mul
from functools import reduce


class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fan = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            fan[i] *= fan[i - 1] or 1
        return max(nums + fan)  #


if __name__ == "__main__":
    s = Solution()
    inpt = [1, 2, -1]
    answer = s.maxProduct(inpt)
    print(answer)
