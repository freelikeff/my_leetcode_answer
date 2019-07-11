#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/5 22:00
# @Author  : frelikeff
# @Site    : 
# @File    : 95answer.py
# @Software: PyCharm
from utils.maketree import TreeNode
from typing import List


# 生成1-n节点组成的所有BST
def helper(nums: List[int]) -> List[TreeNode]:
    if not nums:
        return [None]
    if len(nums) == 1:
        return [TreeNode(nums[0])]
    ans = []
    for i in range(len(nums)):
        lefts = helper(nums[:i])
        rights = helper(nums[i + 1:])
        for l in lefts:
            for r in rights:
                root = TreeNode(nums[i])
                root.left = l
                root.right = r
                ans.append(root)
    return ans


# 感觉不是很好，构造了一个helper函数，传入一个数组，解决了传入由一个排序列表组成的BST，应该会有更方便的解法
# 看了一下，最快的答案和这个思路差不多，那就不多说了
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        assert n >= 0
        if n == 0:
            return []
        if n == 1:
            return [TreeNode(1)]
        return helper([i + 1 for i in range(n)])


if __name__ == '__main__':
    s = Solution()
    for i in range(10):
        print(len(s.generateTrees(i)))
