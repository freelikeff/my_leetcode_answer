#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/19 9:54
# @Author  : frelikeff
# @Site    : 
# @File    : 673answer.py
# @Software: PyCharm
from typing import List


# 这个是求最长递增子序列的长度，354题要用，所以临时写了下，与原题要求不同
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        memo = [nums[0]]
        for item in nums[1:]:
            if item > memo[-1]:
                memo.append(item)
                continue
            for i in range(len(memo)):
                if memo[i] >= item:
                    memo[i] = item
                    break

        return len(memo)


if __name__ == '__main__':
    s = Solution()
    inpt = [2, 1, 5, 3, 6, 4, 8, 9, 3, 7]

    print(s.findNumberOfLIS(inpt))
