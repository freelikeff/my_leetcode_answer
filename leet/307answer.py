#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/3 10:18
# @Author  : frelikeff
# @Site    : 
# @File    : 307answer.py
# @Software: PyCharm
from typing import List


class Binary_Indexed_Trees:
    def __init__(self, nums: List):

        self.tree = [0]
        self.length = len(nums) + 1
        for i in range(len(nums)):
            rank = i + 1

            if rank & 1:
                self.tree.append(nums[i])
            else:
                summ = nums[i]
                det = 1
                while not rank & 1:
                    summ += self.tree[i + 1 - det]
                    det *= 2
                    rank >>= 1
                self.tree.append(summ)
        return

    def change(self, idx, delt):
        rank = idx + 1

        while rank < self.length:
            self.tree[rank] += delt
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


class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.BIT = Binary_Indexed_Trees(nums)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        delt=val-self.nums[i]
        self.BIT.change(i,delt)
        self.nums[i]=val
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if not i:
            return self.BIT.query(j)
        return self.BIT.query(j)-self.BIT.query(i-1)
