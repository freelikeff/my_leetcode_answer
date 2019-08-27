#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/19 9:24
# @Author  : frelikeff
# @Site    : 
# @File    : 354answer.py
# @Software: PyCharm
from typing import List
from functools import cmp_to_key


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        @cmp_to_key
        def my_cmp(a, b):  # 排序的key
            if a[0] == b[0]:
                return b[1] - a[1]
            else:
                return a[0] - b[0]

        def LIS(nums):  # 求最长递增子序列，的长度
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

        envelopes.sort(key=my_cmp)
        return LIS([item[1] for item in envelopes])


if __name__ == '__main__':
    s = Solution()
    envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
    answer = s.maxEnvelopes(envelopes)
    print(answer)
