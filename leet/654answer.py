#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/20 17:12
# @Author  : frelikeff
# @Site    : 
# @File    : 654answer.py
# @Software: PyCharm
from typing import List
from utils.maketree import TreeNode


# 递归，很简单
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])

        maxidx = nums.index(max(nums))
        root = TreeNode(nums[maxidx])
        root.left = self.constructMaximumBinaryTree(nums[:maxidx])
        root.right = self.constructMaximumBinaryTree(nums[maxidx + 1:])
        return root


# 用个单调栈 # TODO
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])

        stack = [TreeNode(nums[0])]
        for i in range(1, len(nums)):
            temp = TreeNode(nums[i])
            if temp.val < stack[-1].val:
                pass
            elif temp.val > stack[0].val:
                while len(stack) > 1:
                    tail = stack.pop()
                    stack[-1].right = tail

                temp.left = stack.pop()
            else:
                while stack[-2].val < temp.val:
                    tail = stack.pop()
                    stack[-1].right = tail

            stack.append(temp)

        while stack > 1:
            tail = stack.pop()
            stack[-1].right = tail
        return stack[0]
