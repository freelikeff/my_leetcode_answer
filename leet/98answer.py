#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/7 10:45
# @Author  : frelikeff
# @Site    : 
# @File    : 98answer.py
# @Software: PyCharm
from utils.maketree import TreeNode, LDRdg


def helper(root: TreeNode) -> (int, int) or bool:  # 如果是二叉搜索树，则返回最小值和最大值，如果不是，则返回False
    assert root
    if not root.left and not root.right:  # 叶节点
        return root.val, root.val
    if not root.left:
        right_part = helper(root.right)
        if not right_part or root.val > right_part[0]:  # 左无右有
            return False
        return root.val, right_part[1]
    if not root.right:
        left_part = helper(root.left)
        if not left_part or root.val < left_part[1]:  # 左有右无
            return False
        return left_part[0], root.val

    # 左右都有
    left_part = helper(root.left)
    if not left_part or root.val < left_part[1]:  # 左有右无
        return False
    else:
        right_part = helper(root.right)
        if not right_part or root.val > right_part[0]:  # 左无右有
            return False
        return left_part[0], right_part[1]


# 效率太低，这谁顶得住，但是思路没啥问题
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        assert root
        if helper(root) is False:
            return False
        return True


# 用一个中序遍历，那么应该是个有序的.效率提升了那么一丢丢，其实还是挺多的时间效率74%
class Solution2:
    def isValidBST(self, root: TreeNode) -> bool:
        assert root
        ans = LDRdg(root)
        for i in range(len(ans) - 1):
            if ans[i] >= ans[i + 1]:
                return False
        return True
