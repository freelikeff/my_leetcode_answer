#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/7 14:33
# @Author  : frelikeff
# @Site    : 
# @File    : 34answer.py
# @Software: PyCharm
from typing import List


def binary_search_left(nums: List, target) -> int:
    # 边界条件
    if not len(nums) or target > nums[-1] or target < nums[0]:
        return -1
    # 左右指针
    if target == nums[0]:
        return 0
    if len(nums) == 1:
        return -1

    i, j = 1, len(nums) - 1
    # 开始二分查找
    while i <= j:
        mid = (i + j) // 2
        if nums[mid] < target:
            i = mid + 1
        elif nums[mid] > target:
            j = mid - 1
        else:  # 相等
            if nums[mid] > nums[mid - 1]:
                return mid
            j = mid - 1
    # 查找中无返回那么此时返回-1
    return -1


def binary_search_right(nums: List, target) -> int:
    # 边界条件
    if not len(nums) or target > nums[-1] or target < nums[0]:
        return -1
    if target == nums[-1]:
        return len(nums) - 1
    if len(nums) == 1:
        return -1

    length = len(nums)
    # 左右指针
    i, j = 0, length - 2
    # 开始二分查找
    while i <= j:
        mid = (i + j) // 2
        if nums[mid] < target:
            i = mid + 1
        elif nums[mid] > target:
            j = mid - 1
        else:  # 相等
            if nums[mid] < nums[mid + 1]:
                return mid
            j = mid - 1
    # 查找中无返回那么此时返回-1
    return -1


from bisect import bisect_left, bisect_right


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # corner case
        if not len(nums) or target < nums[0] or target > nums[-1]:
            return [-1, -1]

        # 左边
        if target == nums[0]:
            left = 0
        else:
            left = bisect_left(nums, target)

            if nums[left] != target:
                left = -1
        # 右边
        if target == nums[-1]:
            right = len(nums) - 1
        else:
            right = bisect_right(nums, target)
            if not right or nums[right - 1] == target:
                right -= 1
            else:
                right = -1
        return [left, right]


class Solution2:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # corner case
        if not len(nums) or target < nums[0] or target > nums[-1]:
            return [-1, -1]
        return [binary_search_left(nums,target),binary_search_right(nums,target)]


if __name__ == '__main__':
    s = Solution2()
    inpt = [5,7,7,8,8,10],8
    answer = s.searchRange(*inpt)
    print(answer)
