#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/9 21:44
# @Author  : frelikeff
# @Site    : 
# @File    : 47answer.py
# @Software: PyCharm
from typing import List


def helper(nums: List[int]) -> List[List[int]]:  # 传入的是一个排序的列表
    if len(nums) == 1:
        return [[nums[0]]]
    ans = []
    for i in range(len(nums)):
        if not i or nums[i] != nums[i - 1]:
            temp = helper(nums[:i] + nums[i + 1:])
            ans.extend(([nums[i]] + item for item in temp))
    return ans


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        return helper(sorted(nums))


if __name__ == '__main__':
    s = Solution()
    inpt = [3,3,0,3]
    ans = s.permuteUnique(inpt)
    print(ans)
