#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/3 15:49
# @Author  : frelikeff
# @Site    : 
# @File    : 173answer.py
# @Software: PyCharm
from utils.maketree import TreeNode, maketree


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        if not root:
            return

        self.stack.append((root, False))

    def next(self) -> int:
        """
        @return the next smallest number
        """
        while self.stack:
            node, flag = self.stack.pop()
            if flag:
                return node.val
            else:
                if node.right:
                    self.stack.append((node.right, False))
                self.stack.append((node, True))
                if node.left:
                    self.stack.append((node.left, False))

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.stack != []


if __name__ == '__main__':
    tree = maketree([4, 2, 1, 3, 6, 5, 7], [1, 2, 3, 4, 5, 6, 7])  # [1, 3, 2, 5, 7, 6, 4]
    s = BSTIterator(tree)
    while s.hasNext():
        print(s.next())
    print("over")
