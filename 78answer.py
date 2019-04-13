#!E:\pycharm\my_venv\Scripts\python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/13 8:50
# @Author  : freelikeff
# @Site    : 
# @File    : 78answer.py
# @Software: PyCharm


# 标准库
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from itertools import combinations
        length = len(nums)
        ans = [nums]
        for i in range(length):
            for item in combinations(nums, i):
                ans.append(list(item))
        return ans


# 这种是我想要的答案，不过是别人的写的，嘿嘿。
class Solution2:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]

        ans = [[]]

        for value in nums:
            temp_result = []
            for valueSet in ans:
                temp_result.append(valueSet + [value])

            ans += temp_result

        return ans


if __name__ == "__main__":
    s = Solution2()
    inpt = [2, 3, 5]
    answer = s.subsets(inpt)
    print(answer)
