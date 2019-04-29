#!D:\coding\my_venv\Scripts\python3
# -*- coding: utf-8 -*- 
# @Time : 2019/4/25 21:06 
# @Author : freelikeff 
# @Site : 
# @File : 238answer.py 
# @Software: PyCharm

from functools import reduce
from operator import mul


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [0 for i in range(len(nums))]
        if nums.count(0) > 1:
            return ans

        if nums.count(0) == 1:
            index0 = nums.index(0)
            value = 1
            for i in range(len(nums)):
                if i != index0:
                    value *= nums[i]
            ans[index0] = value
            return ans

        value = reduce(mul, nums)
        for i in range(len(nums)):
            ans[i] = value // nums[i]

        return ans


if __name__ == "__main__":
    s = Solution()
    inpt = [1, 2, 3, 4]
    answer = s.productExceptSelf(inpt)
    print(answer)
