#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/13 9:21
# @Author  : frelikeff
# @Site    : 
# @File    : heapsort.py
# @Software: PyCharm
from typing import List


def HeapSort(nums: List[int]) -> None:  # 表示就地
    length = len(nums)
    # 边界条件
    if length < 2:
        return

    # 长度大于1时，调整二项堆将当前最大值冒出
    while length > 1:
        maxidx = (length - 2) >> 1
        if nums[maxidx] < nums[2 * maxidx + 1]:
            nums[maxidx], nums[2 * maxidx + 1] = nums[2 * maxidx + 1], nums[maxidx]
        if 2 * maxidx + 2 < length and nums[maxidx] < nums[2 * maxidx + 2]:  # 说明最后一个有右子,且右子需要上游
            nums[maxidx], nums[2 * maxidx + 2] = nums[2 * maxidx + 2], nums[maxidx]

        for idx in range(maxidx - 1, -1, -1):
            if nums[idx] < max(nums[2 * idx + 1], nums[2 * idx + 2]):  # 说明需要调整
                if nums[2 * idx + 1] >= nums[2 * idx + 2]:
                    nums[idx], nums[2 * idx + 1] = nums[2 * idx + 1], nums[idx]
                else:
                    nums[idx], nums[2 * idx + 2] = nums[2 * idx + 2], nums[idx]
        length -= 1
        nums[0], nums[length] = nums[length], nums[0]

    return


if __name__ == '__main__':
    import random

    random.seed(1130)
    for i in range(10):
        nums = random.sample(range(15), 13)

        HeapSort(nums)
        print(nums)
