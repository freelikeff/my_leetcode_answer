#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/23 13:44
# @Author  : frelikeff
# @Site    : 
# @File    : selectionSort.py
# @Software: PyCharm
from typing import List


# 选择排序的交换操作介于 0 和 (n - 1） 次之间。选择排序的比较操作为 n (n - 1） / 2 次之间。选择排序的赋值操作介于 0 和 3 (n - 1） 次之间。
# 比较次数O(n^2），比较次数与关键字的初始状态无关，总的比较次数N=(n-1）+(n-2）+...+1=n*(n-1）/2。交换次数O(n）.
# 最好情况是，已经有序，交换0次；最坏情况交换n-1次，逆序交换n/2次。
# 交换次数比冒泡排序少多了，由于交换所需CPU时间比比较所需的CPU时间多，n值较小时，选择排序比冒泡排序快。
def SelectionSort(nums: List) -> None:
    """
    同样是就地排序
    每次选出剩余序列的最小值放置最前面，所以不稳定（例如[5,5,3]）
    另一方面它的最坏最好平均复杂度都是n方
    """
    if len(nums) < 2:
        return
    start = 0
    while start < len(nums) - 1:
        small = start
        for i in range(start, len(nums)):
            if nums[i] < nums[small]:
                small = i
        if small != start:
            nums[small], nums[start] = nums[start], nums[small]
        start += 1
    return


# 改进版本，之前每次扫描一趟只确定最大值，这次我们直接每一趟确定这趟的最大最小值
def BiSelectionSort(nums: List) -> None:
    if len(nums) < 2:
        return
    start, end = 0, len(nums) - 1  # 老规矩，习惯用全闭区间
    while start < end:
        small, big = start, end
        for i in range(start, end+1):
            if nums[i] < nums[small]:
                small = i
            if nums[i] > nums[big]:
                big = i
        if small != start:
            nums[small], nums[start] = nums[start], nums[small]
        if big != end:
            nums[big], nums[end] = nums[end], nums[big]
        start += 1
        end -= 1
        print(nums,start,end)
    return


if __name__ == '__main__':
    nums = [3, 6, 4, 8, 9, 2, 2, 2, 12, 7, 6]
    BiSelectionSort(nums)
    print(nums)
