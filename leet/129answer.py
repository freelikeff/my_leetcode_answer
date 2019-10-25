#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/28 17:53
# @Author  : frelikeff
# @Site    : 
# @File    : 129answer.py
# @Software: PyCharm
from utils.maketree import TreeNode


def helper(root: TreeNode):
    temp = str(root.val)
    if not root.left and not root.right:
        return [temp]
    elif not root.right:
        return [temp + item for item in helper(root.left)]
    elif not root.left:
        return [temp + item for item in helper(root.right)]
    else:
        return [temp + item for item in helper(root.left)] + [temp + item for item in helper(root.right)]


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans = 0
        for item in helper(root):
            ans += int(item)
        return ans
