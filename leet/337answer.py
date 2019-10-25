#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/5 15:43
# @Author  : frelikeff
# @Site    : 
# @File    : 337answer.py
# @Software: PyCharm
from utils.maketree import TreeNode


def helper(root: TreeNode):  # 返回一个元祖，表示一个树打劫根节点的，值和不打劫根节点的值
    if not root:
        return 0, 0
    if not root.left and not root.right:
        return root.val, 0

    leftpart = helper(root.left)
    rightpart = helper(root.right)

    return root.val + leftpart[1] + rightpart[1], max(max(leftpart)+ max(rightpart))


class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(helper(root))
