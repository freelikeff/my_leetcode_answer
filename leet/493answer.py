#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/1 18:30
# @Author  : frelikeff
# @Site    : 
# @File    : 493answer.py
# @Software: PyCharm
from typing import List


class Binary_Indexed_Trees:
    def __init__(self, length):

        self.tree = [0]
        self.length = length + 1
        self.tree = [0] * self.length

        return

    def change(self, idx):
        rank = idx + 1

        while rank < self.length:
            self.tree[rank] += 1
            rank += Binary_Indexed_Trees.lowbit(rank)

    def query(self, endidx: int):
        rank = endidx + 1
        ans = 0
        while rank:
            ans += self.tree[rank]
            rank &= rank - 1
        return ans

    @staticmethod
    def lowbit(number):
        return number & (-number)


import bisect


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        doubleitems, idx = sorted(map(lambda x: 2 * x, nums)), 0
        my_dict = dict()
        for dou_item in doubleitems:
            my_dict[dou_item] = idx
            idx += 1
        myBIT = Binary_Indexed_Trees(idx)
        ans = 0
        for item in reversed(nums):
            the_idx = my_dict.get(item, bisect.bisect(doubleitems, item))
            if the_idx:
                ans += myBIT.query(the_idx - 1)
            myBIT.change(my_dict[2 * item])
        return ans


if __name__ == '__main__':
    s = Solution()
    inpt = [-5, -5]
    print(s.reversePairs(inpt))
