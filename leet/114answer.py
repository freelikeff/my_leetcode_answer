#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/28 15:59
# @Author  : frelikeff
# @Site    : 
# @File    : 114answer.py
# @Software: PyCharm
from utils.maketree import TreeNode, maketree


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        if not root.left and not root.right:
            return
        elif not root.left:
            self.flatten(root.right)
        elif not root.right:
            self.flatten(root.left)
            root.right = root.left
            root.left = None
        else:
            self.flatten(root.left)
            self.flatten(root.right)
            memo = root.right
            root.right = root.left
            root.left=None
            while root.right:
                root = root.right

            root.right = memo

        return


if __name__ == '__main__':
    mytree = maketree([1, 2, 3, 4, 5, 6], [3, 2, 4, 1, 5, 6])
    s = Solution()
    s.flatten(mytree)
    while mytree:
        print(mytree.left, mytree.right.val)
        mytree = mytree.right
