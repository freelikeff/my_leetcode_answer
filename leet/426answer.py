#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/26 19:43
# @Author  : frelikeff
# @Site    : https://blog.csdn.net/u010005281/article/details/79657259
# @File    : 426answer.py
# @Software: PyCharm


class Solution:
    def __init__(self):
        self.listHead = None
        self.listTail = None

    # 将二叉树转换为有序双向链表
    def Convert(self, pRootOfTree):
        if not pRootOfTree :
            return
        self.Convert(pRootOfTree.left)
        if not self.listHead :
            self.listHead = pRootOfTree
            self.listTail = pRootOfTree
        else:
            self.listTail.right = pRootOfTree
            pRootOfTree.left = self.listTail
            self.listTail = pRootOfTree
        self.Convert(pRootOfTree.right)
        return self.listHead

    # 获得链表的正向序和反向序
    def printList(self, head):
        while head.right:
            print(head.val, end=" ")
            head = head.right
        print(head.val)
        while head:
            print(head.val, end=" ")
            head = head.left

    # 给定二叉树的前序遍历和中序遍历，获得该二叉树
    def getBSTwithPreTin(self, pre, tin):
        if len(pre) == 0 | len(tin) == 0:
            return None

        root = TreeNode(pre[0])
        for order, item in enumerate(tin):
            if root.val == item:
                root.left = self.getBSTwithPreTin(pre[1:order + 1], tin[:order])
                root.right = self.getBSTwithPreTin(pre[order + 1:], tin[order + 1:])
                return root


class TreeNode:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x


if __name__ == '__main__':
    s = Solution()
    preorder_seq = [4, 2, 1, 3, 6, 5, 7]
    middleorder_seq = [1, 2, 3, 4, 5, 6, 7]
    treeRoot1 = s.getBSTwithPreTin(preorder_seq, middleorder_seq)
    head = s.Convert(treeRoot1)
    s.printList(head)

    #      4
    #    /   \
    #   2     6
    #  / \   / \
    # 1   3 5   7
