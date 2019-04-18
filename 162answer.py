#!E:\pycharm\my_venv\Scripts\python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 8:39
# @Author  : freelikeff
# @Site    : 
# @File    : 162answer.py
# @Software: PyCharm


# 看别人有用二分，觉得没必要，这个直接一路扫过去，返回第一个找到的比后一个元素大的元素的索引即可
# 因为是第一个，所以前一个元素比他小，如果扫到最后也没有，那直接返回最后一个索引即可
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i
        return len(nums)-1


if __name__ == "__main__":
    s = Solution()
    inpt = [1, 2, 1, 3, 5, 6, 4]
    ans = s.findPeakElement(inpt)
    print(ans)
