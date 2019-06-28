#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/23 18:15
# @Author  : frelikeff
# @Site    : 
# @File    : 230answer.py
# @Software: PyCharm
from utils.maketree import TreeNode,LDRdg

# 由于是BST，所以直接中序遍历，返回index=k-1即可
# 效率并不高，其实也还行
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        return LDRdg(root)[k-1]