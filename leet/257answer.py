#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/7 11:49
# @Author  : frelikeff
# @Site    : 
# @File    : 257answer.py
# @Software: PyCharm
from utils.maketree import TreeNode
from typing import List

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        ans=[]
        temp=str(root.val)+"->"
        for item in self.binaryTreePaths(root.left):
            ans.append(temp+item)
        for item in self.binaryTreePaths(root.right):
            ans.append(temp+item)

        return ans

