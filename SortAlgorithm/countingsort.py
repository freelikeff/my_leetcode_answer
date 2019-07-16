#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/12 9:20
# @Author  : frelikeff
# @Site    : 
# @File    : countingsort.py
# @Software: PyCharm
from typing import List


# 计数排序应用于数据比较集中，重复较多，这样把每个数据重复的次数记下来，然后拼接即可。
# 所以有特定的应用场景，时间复杂度O(n+k),空间复杂度O(n+k)
# 可就地也可非就地
def CountingSort(nums: List[int], sortfunc, rate: int = 0.3) -> List[int]:
    if len(nums) < 2:
        return nums
    maxx, minn = max(nums), min(nums)
    length = maxx - minn + 1

    # 如果装填因子太大（参数可设定），说明计数排序意义不大，那么用其他排序方法
    if length / len(nums) > rate:
        print("change sort algorithm")
        return sortfunc(nums)

    # 计数数组和答案数组初始化
    count_arr = [0] * length
    ans = [0] * len(nums)

    # 进行计数，时间复杂度线性
    for item in nums:
        count_arr[item - minn] += 1

    # 接下来的一系列操作是为了保证稳定性
    for i in range(1, length):
        count_arr[i] += count_arr[i - 1]

    # 反向扫描
    for i in range(len(nums) - 1, -1, -1):
        ans[count_arr[nums[i] - minn] - 1] = nums[i]
        count_arr[nums[i] - minn] -= 1
    return ans


if __name__ == '__main__':
    import random
    from SortAlgorithm.quicksort import QuickSort_dg

    random.seed(1130)

    for i in range(10):
        nums = random.choices(range(10, 15), k=30)
        print(CountingSort(nums, QuickSort_dg))
