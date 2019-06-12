#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/9 11:08
# @Author  : frelikeff
# @Site    : 
# @File    : 101symmetric_tree.py
# @Software: PyCharm
from utils.maketree import TreeNode


def mirro(s: TreeNode, t: TreeNode) -> bool:
    if not s and not t:
        return True
    if not s or not t:
        return False
    return s.val == t.val and mirro(s.left, t.right) and mirro(s.right, t.left)


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return mirro(root.left, root.right)
