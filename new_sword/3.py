#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/11 18:49
# @Author  : frelikeff
# @Site    : 442answer
# @File    : 3.py
# @Software: PyCharm
from typing import List


# 442 是数组中的数组只可能出现一次或两次,范围1->n 找出所有出现两次的值
# 这个题是不知道重复的重复了几次，范围0->n-1，找出一个重复值即可
def findRepeat(nums: List[int]) -> int:
    assert len(nums) > 1
    for i in range(len(nums)):
        nums[i] += 1
    for item in nums:
        idx = abs(item) - 1
        if nums[idx] > 0:
            nums[idx] = -nums[idx]
        else:
            return idx


# 这是书上的算法
# 对于每个idx上的数字m，如果idx=m,那么说明排序后它就应该在这个位置上，那么idx+=1
# 如果idx！=m,那么我们找到nums[m]，如果nums[m]=m，return m；如果！=，那么久把将idx与m做交换，先把m这个数字安置好
def findRepeat2(nums: List[int]) -> int:
    assert len(nums) > 1
    for i in range(len(nums)):
        while i != nums[i]:
            if nums[i] == nums[nums[i]]:
                return nums[i]
            else:
                temp = nums[i]
                nums[i], nums[temp] = nums[temp], nums[i]


inpt = [0, 0, 0]
print(findRepeat2(inpt))
