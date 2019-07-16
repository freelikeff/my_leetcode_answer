#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/23 13:57
# @Author  : frelikeff
# @Site    : 
# @File    : insertionSort.py
# @Software: PyCharm

from typing import List


# 可优化至二分查找，略
# 稳定
def InsertSort(nums: List) -> None:
    """
    就地排序
    """
    if len(nums) < 2:
        return
    for i in range(1, len(nums)):
        if nums[i] < nums[0]:
            nums[0], nums[1:i + 1] = nums[i], nums[:i]
            continue
        elif nums[i] >= nums[i - 1]:  # 这一步保证如果完全有序，那么时间复杂度变为线性
            continue
        for j in range(i - 1):
            if nums[j] <= nums[i] < nums[j + 1]:
                nums[j + 1], nums[j + 2:i + 1] = nums[i], nums[j + 1:i]

    return


if __name__ == '__main__':
    import random

    random.seed(1130)
    for i in range(10):
        nums = random.sample(range(1000), 20)
        InsertSort(nums)
        print(nums)
