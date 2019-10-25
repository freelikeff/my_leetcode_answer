#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/20 20:54
# @Author  : frelikeff
# @Site    : 
# @File    : TraverseTree.py
# @Software: PyCharm
"""
LR代表左右，D代表根
整理了一下前中后的递归非递归遍历
以及层次遍历
"""
from utils.maketree import TreeNode, maketree


# 前序遍历 Preorder Traversal
class PreorderTraversal:
    # 递归的就没什么好描述了
    def DLR_dg(self, root: TreeNode):
        if not root:
            return []
        return [root.val] + self.DLR_dg(root.left) + self.DLR_dg(root.right)

    # 简单来说就是自构栈，每次访问一个节点后，就把右节点和左节点入栈，如果有的话
    # 那么这样顺序就是根，左（因为是栈），右
    def DLR_ndg(self, root: TreeNode):
        if not root:
            return []
        stack = [root]
        ans = []
        while stack:
            temp = stack.pop()
            ans.append(temp.val)
            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)

        return ans


# 中序遍历
class MidorderTraversal:
    # 递归的就没什么好描述了
    def LdR_dg(self, root: TreeNode):
        if not root:
            return []
        return self.LdR_dg(root.left) + [root.val] + self.LdR_dg(root.right)

    def LdR_ndg(self, root: TreeNode):
        if not root:
            return []


if __name__ == '__main__':
    tree = maketree([4, 2, 1, 3, 6, 5, 7], [1, 2, 3, 4, 5, 6, 7])
    s = MidorderTraversal()
    print(s.LdR_dg(tree))
