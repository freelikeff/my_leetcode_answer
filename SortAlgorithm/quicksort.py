#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/8 11:44
# @Author  : frelikeff
# @Site    : 
# @File    : quicksort.py
# @Software: PyCharm
from typing import List


# 递归
def QuickSort_dg(nums: List[int]) -> List[int]:  # 老规矩，个人习惯，左右都闭
    if len(nums) <= 1:
        return nums
    basenums = nums[random.randrange(len(nums))]
    return QuickSort_dg([item for item in nums if item < basenums]) + [basenums] * nums.count(basenums) + QuickSort_dg(
        [item for item in nums if item > basenums])


# in-place
def QuivkSort_inplace(nums: List[int], start, end) -> None:  # 老规矩，个人习惯，左右都闭
    if end <= start:
        return
    basenums = nums[random.randrange(len(nums))]
    i, j = start, end
    while i < j:
        if nums[i] > basenums >= nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        elif nums[i] <= basenums < nums[j]:
            i += 1
            j -= 1
        elif nums[i] <= basenums:
            i += 1
        else:
            j -= 1
    if i == j:
        if nums[i] <= basenums:
            QuivkSort_inplace(nums, start, i)
            QuivkSort_inplace(nums, i + 1, end)
        else:
            QuivkSort_inplace(nums, start, i - 1)
            QuivkSort_inplace(nums, i, end)
    else:
        QuivkSort_inplace(nums, start, j)
        QuivkSort_inplace(nums, i, end)


if __name__ == '__main__':
    import random

    random.seed(1130)
    for i in range(10):
        nums = random.sample(range(1000), 20)
        print(QuickSort_dg(nums))
        QuivkSort_inplace(nums, 0, len(nums) - 1)
        print(nums)
