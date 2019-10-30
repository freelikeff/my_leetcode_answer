#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/28 10:09
# @Author  : frelikeff
# @Site    : 
# @File    : binary_indexed_trees.py
# @Software: PyCharm
"""
树状数组实现
"""
from typing import List


class Binary_Indexed_Trees:
    def __init__(self, nums: List):

        self.tree = [0]
        self.length = len(nums) + 1
        for i in range(len(nums)):
            rank = i + 1
            summ = nums[i]
            if rank & 1:
                self.tree.append(nums[i])
            else:
                summ = 0

                # 第一种实现方法，直接从当前数往前加2^k个
                # for n in range(Binary_Indexed_Trees.lowbit(rank)):
                #     summ += nums[i - n]
                # self.tree.append(summ)

                # 第二种方法，直接调用树状数组之前的结果
                summ = nums[i]
                det = 1
                while not rank & 1:
                    summ += self.tree[i+1-det]
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


if __name__ == '__main__':
    nums = [1, 5, 10, 12, 19, 22, 23, 24, 25, 27, 30, 31, 33, 34, 35, 36]
    myBIT = Binary_Indexed_Trees(nums)
    print(myBIT.tree)
    for i in range(len(nums)):
        trueans = sum(nums[:i + 1])
        myans = myBIT.query(i)
        print(trueans, myans)

    nums[5]+=4
    myBIT.change(5,4)
    for i in range(len(nums)):
        trueans = sum(nums[:i + 1])
        myans = myBIT.query(i)
        print(trueans, myans)