#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/8 11:44
# @Author  : frelikeff
# @Site    : 
# @File    : quicksort.py
# @Software: PyCharm
from typing import List


# 递归，如果是这样的快排，那么是稳定的
def QuickSort_dg(nums: List[int]) -> List[int]:  # 老规矩，个人习惯，左右都闭
    if len(nums) <= 1:
        return nums
    basenums = nums[random.randrange(len(nums))]
    return QuickSort_dg([item for item in nums if item < basenums]) + [basenums] * nums.count(basenums) + QuickSort_dg(
        [item for item in nums if item > basenums])


# in-place
def QuickSort_inplace(nums: List[int], start, end) -> None:  # 老规矩，个人习惯，左右都闭
    if end <= start:
        return
    basenums = nums[random.randrange(len(nums))]
    i, j = start, end
    while i < j:  # 交换会导致不稳定
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
            QuickSort_inplace(nums, start, i)
            QuickSort_inplace(nums, i + 1, end)
        else:
            QuickSort_inplace(nums, start, i - 1)
            QuickSort_inplace(nums, i, end)
    else:
        QuickSort_inplace(nums, start, j)
        QuickSort_inplace(nums, i, end)


# 非递归，那么需要用到栈
def QuickSort_ndg(nums: List[int]) -> None:
    if len(nums) < 2:
        return
    stack = [0, len(nums) - 1]
    while stack:
        right = stack.pop()
        left = stack.pop()

        front_end, behind_start = partition(nums, left, right)
        if left < front_end:
            stack.append(left)
            stack.append(front_end)
        if right > behind_start:
            stack.append(behind_start)
            stack.append(right)

    return


def partition(nums, start, end):  # 个人习惯，全是闭区间
    """

    :param nums: 需要排序的数组
    :param start: partition的起点idx
    :param end: partition的终点idx
    :return: 前一部分的终点and后一部分的起点
    """
    assert start < end
    if start == end - 1:
        if nums[start] > nums[end]:
            nums[start], nums[end] = nums[end], nums[start]
        return start, end  # 这里返回什么已经没有意义了，因为不需要再分治了

    basenums = nums[random.randrange(start, end + 1)]
    while start < end:
        if nums[start] > basenums >= nums[end]:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        elif nums[start] <= basenums < nums[end]:
            start += 1
            end -= 1
        elif nums[start] <= basenums:
            start += 1
        else:
            end -= 1

    if start == end:
        if nums[start] > basenums:
            return start - 1, start
        else:
            return start, start + 1
    else:
        return end, start


if __name__ == '__main__':
    import random
    from SortAlgorithm.testit import test_sorted
    random.seed(1130)
    for i in range(1):
        nums = random.sample(range(40), 16)
        QuickSort_ndg(nums)
        print(nums,end="  ")
        print(test_sorted(nums))
