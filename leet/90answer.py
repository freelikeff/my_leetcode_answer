#!E:\pycharm\my_venv\Scripts\python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/20 16:23
# @Author  : freelikeff
# @Site    : 
# @File    : 90answer.py
# @Software: PyCharm

from itertools import combinations


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
       """
        my_list = sorted(nums)
        ans = []
        for i in range(len(nums) + 1):
            ans += list(set(combinations(my_list, i)))

        return ans


if __name__ == '__main__':
    s = Solution()
    inpt = [1, 2, 2, 3, 3, 3]
    answer = s.subsetsWithDup(inpt)
    print(answer)
