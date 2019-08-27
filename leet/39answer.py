#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 14:29
# @Author  : frelikeff
# @Site    : 
# @File    : 39answer.py
# @Software: PyCharm
from typing import List
from bisect import bisect_left


def helper(sorted_num: List[int], target, start):  # 底层，首先让数组有序并且没有重复（因为重复没有意义）,传入起始idx
    if sorted_num[start] == target:
        return [[target]]
    if sorted_num[start] > target:
        return None
    ans = [[target]] if target in sorted_num else []
    end = bisect_left(sorted_num, target)
    for i in range(start, end):
        temp = helper(sorted_num, target - sorted_num[i], i)
        if temp:
            ans += [[sorted_num[i]] + item for item in temp]
    return ans


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        if target in candidates:
            ans.append([target])
        my_cand = sorted([item for item in list(set(candidates)) if item < target])
        if not my_cand:
            return []
        return helper(my_cand, target, 0)


if __name__ == '__main__':
    s = Solution()
    inpt = [2, 5], 3
    answer = s.combinationSum(*inpt)
    print(answer)
