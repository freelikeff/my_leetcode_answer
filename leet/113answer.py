#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/24 16:20
# @Author  : frelikeff
# @Site    : 
# @File    : 113answer.py
# @Software: PyCharm
from utils.maketree import TreeNode
from typing import List


# def helper(root: TreeNode, sum: int)-> List[List[int]]:
#     if not root:
#         return []
#     if not root.left and not root.right:
#         if root.val==sum:
#             return [[sum]]
#         else:
#             return []
#     ans=[]
#     leftans=helper(root.left,sum-root.val)
#     rightans=helper(root.right,sum-root.val)
#     if leftans:
#         ans.extend(([root.val]+item for item in leftans))
#     if rightans:
#         ans.extend(([root.val] + item for item in rightans))
#     return ans
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        if not root.left and not root.right:
            if root.val == sum:
                return [[sum]]
            else:
                return []
        ans = []
        leftans = self.pathSum(root.left, sum - root.val)
        rightans = self.pathSum(root.right, sum - root.val)
        if leftans:
            ans.extend(([root.val] + item for item in leftans))
        if rightans:
            ans.extend(([root.val] + item for item in rightans))
        return ans


if __name__ == '__main__':
    pass
