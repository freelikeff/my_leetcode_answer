#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/1 18:36
# @Author  : frelikeff
# @Site    : 
# @File    : 144answer.py
# @Software: PyCharm
"""
给定一个二叉树，返回它的 前序 遍历。

 示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,2,3]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
"""
from utils.maketree import TreeNode
from typing import List


# 递归
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:

        if not root:
            return []
        else:
            return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)


# 人工栈。非递归.
# 两个额外空间，人工栈，ans列表
# 如果根节点为空，直接返回空列表
# 如果根节点不为空，那么把根节点压入栈
# 开始迭代，每次栈pop一个节点，将值列入ans，然后将这个节点的右子节点压入栈（如果存在），接着讲左节点压入栈（如果存在），知道栈空
# 上述稍微解释一下，因为是DLR，所以现将右子节点入栈
class Solution2:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        ans = []
        if not root:
            return ans
        stack.append(root)
        while stack:
            node = stack.pop()
            ans.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return ans


# 没看懂
class Solution3:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        ans = []
        while root or stack:
            while root:
                ans.append(root.val)
                stack.append(root)
                root = root.left
            if stack:
                cur_node = stack.pop()
                root = cur_node.right
        return ans
