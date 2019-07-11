#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/7 22:02
# @Author  : frelikeff
# @Site    : 
# @File    : mergesort.py
# @Software: PyCharm
from typing import List


# 有返回的，所以不是就地排序，那么就有额外的空间复杂度
def helper_dg(anums, bnums):  # 将两个有序列表合并成一个有序列表
    if not anums:
        return bnums
    if not bnums:
        return anums
    if anums[-1] <= bnums[0]:
        return anums + bnums
    if bnums[-1] <= anums[0]:
        return bnums + anums
    i, j = 0, 0
    ans = []
    while i < len(anums) and j < len(bnums):
        if anums[i] <= bnums[j]:  # 这里保证稳定性
            ans.append(anums[i])
            i += 1
        else:
            ans.append(bnums[j])
            j += 1
    if i == len(anums):
        return ans + bnums[j:]
    else:
        return ans + anums[i:]


# 这样的话每次都会递归调用都需要开辟额外数组,严格来说空间复杂度就不是O（n）：TODO
def MergeSort_dg(nums: List[int]) -> List[int]:
    if len(nums) < 2:
        return nums
    mid = len(nums) // 2
    return helper_dg(MergeSort_dg(nums[:mid]), MergeSort_dg(nums[mid:]))


if __name__ == '__main__':
    import random

    random.seed(1130)
    for i in range(10):
        nums = random.sample(range(1000), 100)
        print(MergeSort_dg(nums))
