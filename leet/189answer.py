#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/7 21:14
# @Author  : frelikeff
# @Site    : 
# @File    : 189answer.py
# @Software: PyCharm
from typing import List

# 就地，进行三次反转即可
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        length = len(nums)
        # 取个余
        k %= length
        if k == 0:
            return
        for i in range(length // 2):
            nums[i], nums[length - 1 - i] = nums[length - 1 - i], nums[i]
        print(nums)
        for i in range(k//2):
            nums[i], nums[k - 1 - i] = nums[k - 1 - i], nums[i]
        print(nums)
        for i in range(k,(length-k)//2+k):
            nums[i], nums[length +k-1 - i] = nums[length +k- 1 - i], nums[i]


if __name__ == '__main__':
    s=Solution()
    nums=[1,2,3,4,5,6,7]
    k=10
    s.rotate(nums,k)
    print(nums)