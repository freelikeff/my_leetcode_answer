#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/23 16:22
# @Author  : frelikeff
# @Site    : 
# @File    : 110answer.py
# @Software: PyCharm
from utils.maketree import TreeNode


# 根据概念最简单的递归，但是时间效率必然很差
def helper(root: TreeNode):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    left_part = helper(root.left)
    right_part = helper(root.right)
    if type(left_part) is not int or type(right_part) is not int:
        return False
    if abs(left_part - right_part) < 2:
        return max(left_part, right_part) + 1
    else:
        return False


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if helper(root) is False:
            return False
        return True


if __name__ == '__main__':
    from utils.maketree import maketree

    mytree = maketree([1, 2, 4, 6, 7, 5, 3], [6, 4, 7, 2, 5, 1, 3])
    s=Solution()
    ans=s.isBalanced(mytree)
    print(ans)