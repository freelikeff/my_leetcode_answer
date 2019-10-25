#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/22 22:20
# @Author  : frelikeff
# @Site    : 
# @File    : bubbleSort.py
# @Software: PyCharm
from typing import List


# 设置标记的冒泡排序
def BubbleSort(nums: List) -> None:
    # 边界条件
    if len(nums) < 2:
        return
        # 返回的是None，代表就地排序
    for epoch in range(len(nums), 1, -1):
        flag = True  # 设置标记位，如果某一趟冒泡没有进行交换，那么说明已经排序好了，任务完成
        for j in range(1, epoch):
            if nums[j] < nums[j - 1]:  # 这里相等不交换，则是稳定排序
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                flag = False
        if flag:
            return
    return


# 鸡尾酒排序。冒泡排序的改进。
# 冒泡排序只是从低到高，一直把最大值冒泡至最高处，而鸡尾酒排序是从低到高从高到低交叉进行
# 以序列(2,3,4,5,1)为例，鸡尾酒排序只需要从低到高，然后从高到低就可以完成排序，但如果使用冒泡排序则需要四次。
# 但是在乱数序列的状态下，鸡尾酒排序与冒泡排序的效率都很差劲。
def CocktailSort(nums: List) -> None:
    # 边界条件
    if len(nums) < 2:
        return
        # 返回的是None，代表就地排序

    left, right = 0, len(nums) - 1  # 个人习惯使用全闭区间
    low_high_flag = True  # 这个表示正还是反
    while left < right:
        flag = True  # 这是表示是epoch是否进行交换，True代表没有交换，说明剩下的已经有序，可以直接返回了
        if low_high_flag:  # 表示正
            for i in range(left + 1, right + 1):
                if nums[i] < nums[i - 1]:
                    nums[i], nums[i - 1] = nums[i - 1], nums[i]
                    flag = False
            right -= 1
        else:  # 表示反
            for i in range(right, left, -1):
                if nums[i] < nums[i - 1]:
                    nums[i], nums[i - 1] = nums[i - 1], nums[i]
                    flag = False
            left += 1
        if flag:
            return
        low_high_flag = not low_high_flag
    return


if __name__ == '__main__':
    import random

    random.seed(1130)
    for i in range(10):
        nums = random.sample(range(20), 10)
        print(nums)
        CocktailSort(nums)
        print(nums)
