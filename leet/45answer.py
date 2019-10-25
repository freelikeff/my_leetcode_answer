#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/21 14:11
# @Author  : frelikeff
# @Site    : 
# @File    : 45answer.py
# @Software: PyCharm
from typing import List


# 多好的dp，可惜超时了-_-
class Solution:
    def jump(self, nums: List[int]) -> int:
        # 先逆序，这样代码精简一点
        nums.reverse()
        dp = []
        for i, item in enumerate(nums):
            if item >= i:
                dp.append(1)
            elif item:
                dp.append(1 + min(dp[i - item:i]))
            else:
                dp.append(1 << 15)
        # print(dp)
        return dp[-1]


# 有点类似于BFS,一直扩充最远边界
class Solution2:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        off = len(nums)
        start = 1
        end = nums[0]
        step = 1
        while end < off-1:

            step += 1
            maxx = end
            for i in range(start, end + 1):
                if i + nums[i] > maxx:
                    maxx = i + nums[i]
            start, end = end + 1, maxx
        return step


if __name__ == '__main__':
    s = Solution2()
    inpt = [2, 3, 1, 1, 4]
    print(s.jump(inpt))
