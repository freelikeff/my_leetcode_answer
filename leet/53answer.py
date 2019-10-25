#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/9 13:17
# @Author  : frelikeff
# @Site    : 
# @File    : 53answer.py
# @Software: PyCharm
from typing import List


# 经典dp
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [nums[0]]
        for item in nums[1:]:
            if dp[-1] > 0:
                dp.append(dp[-1] + item)
            else:
                dp.append(item)
        return max(dp)


# 分治，思想挺好的。
def helper(nums, flag=True):
    if len(nums) == 1:
        return nums[0]
    if not nums:
        return 0
    maxx, summ = float("-inf"),0
    if flag:  # 从前往后计算最大值
        for item in nums:
            summ += item
            if summ > maxx:
                maxx = summ
    else:
        for item in reversed(nums):
            summ += item
            if summ > maxx:
                maxx = summ
    return maxx


class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if not nums:
            return 0
        return max(self.maxSubArray(nums[:len(nums) // 2]), self.maxSubArray(nums[len(nums) // 2:]),
                   helper(nums[:len(nums) // 2], False) + helper(nums[len(nums) // 2:]))


if __name__ == '__main__':
    s = Solution2()
    inpt = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    answer = s.maxSubArray(inpt)
    print(answer)
