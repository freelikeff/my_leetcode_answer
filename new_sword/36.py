#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/13 10:14
# @Author  : frelikeff
# @Site    : 426answer
# @File    : 36.py
# @Software: PyCharm


from utils.maketree import TreeNode, maketree


def convert_two(root: TreeNode):
    if not root:
        return None, None
    if not root.left and not root.right:
        return root, root
    if not root.right:
        left_part = convert_two(root.left)
        left_part[1].right = root
        root.left = left_part[1]
        return left_part[0], root
    elif not root.left:
        right_part = convert_two(root.right)
        right_part[0].left = root
        root.right = right_part[0]
        return root, right_part[1]
    else:
        left_part = convert_two(root.left)
        left_part[1].right = root
        root.left = left_part[1]
        right_part = convert_two(root.right)
        right_part[0].left = root
        root.right = right_part[0]
        return left_part[0], right_part[1]


class Solution:
    # 将二叉树转换为有序双向链表
    def Convert(self, root):
        return convert_two(root)[0]

    # 获得链表的正向序和反向序
    def printList(self, head):
        while head.right:
            print(head.val, end=" ")
            head = head.right
        print(head.val)
        while head:
            print(head.val, end=" ")
            head = head.left


if __name__ == '__main__':
    s = Solution()
    preorder_seq = [4, 2, 1, 3, 6, 5, 7]
    middleorder_seq = [1, 2, 3, 4, 5, 6, 7]
    treeRoot1 = maketree(preorder_seq, middleorder_seq)
    head = s.Convert(treeRoot1)
    s.printList(head)

    #      4
    #    /   \
    #   2     6
    #  / \   / \
    # 1   3 5   7
