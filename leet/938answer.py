#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/5 16:47
# @Author  : frelikeff
# @Site    : 
# @File    : 938answer.py
# @Software: PyCharm
from utils.maketree import TreeNode
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        if root.val<L:
            return self.rangeSumBST(root.right,L,R)
        if root.val>R:
            return self.rangeSumBST(root.left,L,R)
        else:
            return self.rangeSumBST(root.right,L,R)+self.rangeSumBST(root.left,L,R)+root.val




