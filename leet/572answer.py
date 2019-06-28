#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/2 10:00
# @Author  : frelikeff
# @Site    : 
# @File    : 572answer.py
# @Software: PyCharm
from utils.maketree import TreeNode


def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True
    elif not p or not q:
        return False
    elif p.val == q.val:
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    else:
        return False


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if isSameTree(s, t):
            return True
        if not s:
            return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
