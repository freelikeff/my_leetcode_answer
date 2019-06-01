#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/1 19:18
# @Author  : frelikeff
# @Site    : 
# @File    : 94answer.py
# @Software: PyCharm

"""
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
"""
from utils.maketree import TreeNode
from typing import List


# 递归
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # if not root:
        #     return []
        # return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        stack = []
        ans = []
        cur = root
        while cur or stack:  #
            while cur:
                stack.append(cur)
                cur = cur.left
            if stack:
                p = stack.pop()
                ans.append(p.val)
                cur = p.right
        return ans
