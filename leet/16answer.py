#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/26 15:21
# @Author  : frelikeff
# @Site    : 
# @File    : 16answer.py
# @Software: PyCharm
from typing import List
from sys import maxsize


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        mindet = maxsize
        ans = 0
        nums.sort()
        for i in range(len(nums) - 2):
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                det = nums[i] + nums[left] + nums[right] - target
                if abs(det) < mindet:
                    mindet = abs(det)
                    ans = det + target
                if det == 0:
                    return ans
                elif det > 0:
                    right -= 1
                else:
                    left += 1
        return ans


if __name__ == "__main__":
    s = Solution()
    inpt = [-1, 2, 1, -4], 1
    answer = s.threeSumClosest(*inpt)
    print(answer)
