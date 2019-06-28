#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/8 10:34
# @Author  : frelikeff
# @Site    : 
# @File    : 104answer.py
# @Software: PyCharm
from utils.maketree import TreeNode


# 递归的思路很简单，代码也好看
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# 不递归,那就人工栈，DFS
class Solution2:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(1, root)]
        depth = 1
        while stack:
            temp_depth, temp_node = stack.pop()
            if temp_node:
                if temp_depth > depth:
                    depth = temp_depth
                stack.append((temp_depth + 1, temp_node.left))
                stack.append((temp_depth + 1, temp_node.right))
        return depth
