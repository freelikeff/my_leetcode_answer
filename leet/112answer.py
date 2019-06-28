#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/29 9:58
# @Author  : frelikeff
# @Site    : 
# @File    : 112answer.py
# @Software: PyCharm
from typing import List
"""
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 经典递归
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return sum == root.val
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)


# 人工栈
class Solution2:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        valu = 0
        stack = [(valu, root), ]
        while stack:
            v, rt = stack.pop()
            if rt.left is None and rt.right is None:  # 意味着是个叶子节点
                if v + rt.val == sum:
                    return True
            if rt.right:  # 右子节点入栈
                stack.append((v + rt.val, rt.right))
            if rt.left:
                stack.append((v + rt.val, rt.left))
        return False

# 加大难度，打印出所有路径
class Solution3:  # TODO
    def hasPathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        return False

