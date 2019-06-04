#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/30 15:43
# @Author  : frelikeff
# @Site    : 
# @File    : micro11.py
# @Software: PyCharm
"""
题目：输入一颗二元查找树，将该树转换为它的镜像，即在转换后的二元查找树中，左子树的结点都大于
右子树的结点。用递归和循环两种方法完成树的镜像转换。
例如输入：
8
/ \
6 10
/\ /\
5 7 9 11
输出：
8
/ \
10 6
/\ /\
11 9 7 5
"""
from utils.maketree import maketree, TreeNode,LDRdg,DLRdg


class Solution:
    # 镜像对称转换
    def MirrorRecursively(self, root: TreeNode) -> TreeNode or None:
        if not root:
            return None

        root.left, root.right = self.MirrorRecursively(root.right), self.MirrorRecursively(
            root.left)
        return root


if __name__ == '__main__':
    s=Solution()
    my_tree = maketree([4, 2, 1, 3, 6, 5, 7], [1, 2, 3, 4, 5, 6, 7])
    ans = s.MirrorRecursively(my_tree)
    print(LDRdg(ans))
    print(DLRdg(ans))
