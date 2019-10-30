#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/29 16:04
# @Author  : frelikeff
# @Site    : 
# @File    : 315answer.py
# @Software: PyCharm
from typing import List


class Binary_Indexed_Trees:
    def __init__(self, nums: List):

        self.tree = [0]
        self.length = len(nums) + 1
        for i in range(len(nums)):
            rank = i + 1
            summ = nums[i]

            det = 1
            while not rank & 1:
                summ += self.tree[i + 1 - det]
                det *= 2
                rank >>= 1
            self.tree.append(summ)
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


# 得到一个列表对应的从小到大排列的rank，从1开始，相同的元素rank相同且rank值连续
def get_unique_rank(nums: List) -> iter:
    mydict = {item: i + 1 for i, item in enumerate(sorted(set(nums)))}
    return [mydict[item] for item in nums]


class Solution1:
    def countSmaller(self, nums: List[int]) -> List[int]:
        rank = get_unique_rank(nums)[::-1]
        BIT = Binary_Indexed_Trees([0] * (len(rank) + 1))
        ans = []
        for r in rank:
            BIT.change(r)
            ans.append(BIT.query(r - 1))
        return ans[::-1]


# 利用一个二分查找树，不需要平衡，每次插入的时候记住往右边走了几次，表示有多少比他小的。
class Treenode:
    def __init__(self, value):
        self.val = value
        self.cou = 1
        self.lcou = 0
        self.left = None
        self.right = None


class Tree:
    def __init__(self, node: Treenode):
        self.start = node

    def insert(self, node: Treenode):
        temp = self.start
        count = 0
        while temp:
            if node.val < temp.val:
                temp.lcou += 1
                if not temp.left:
                    temp.left = node
                    break
                else:
                    temp = temp.left
            elif node.val > temp.val:
                count += (temp.cou+temp.lcou)
                if not temp.right:
                    temp.right = node
                    break
                else:
                    temp = temp.right
            else:
                temp.cou += 1
                count+=temp.lcou
                break
        return count


class Solution2:
    def countSmaller(self, nums: List[int]) -> List[int]:
        length = len(nums)
        if not length:
            return []
        if length == 1:
            return [0]
        ans = [0]
        mytree = Tree(Treenode(nums[-1]))
        for i in range(0, len(nums) - 1):
            ans.append(mytree.insert(Treenode(nums[length - 2 - i])))
        return ans[::-1]


if __name__ == '__main__':
    s = Solution2()
    inpt = [26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41]
    print(s.countSmaller(inpt))
