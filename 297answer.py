#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/16 10:05
# @Author  : frelikeff
# @Site    : 
# @File    : 297answer.py
# @Software: PyCharm
from utils.maketree import TreeNode


class Codec:
    def serialize(self, root: TreeNode) -> str:
        """
        层次遍历的画蛇添足版（非贬义），考虑了叶节点的左右子节点（None）
        """

        if not root:
            return ""
        ans = []
        stack = [root]
        while stack:
            next_stack = []
            for node in stack:
                if node:
                    ans.append(node.val)
                    next_stack.extend([node.left, node.right])
                else:
                    ans.append(None)
            stack = next_stack
        return ",".join([str(item) for item in ans])

    def deserialize(self, data: str) -> TreeNode or None:
        """
        Decodes your encoded data to tree.
        """
        if not data:
            return None
        values = data.split(sep=",")
        root = TreeNode(int(values[0]))
        stack = [root]
        i = 1
        while stack:
            next_stack = []
            for node in stack:
                if i == len(values):
                    break
                if values[i] != "None":
                    node.left = TreeNode(int(values[i]))
                    next_stack.append(node.left)
                i += 1
                if values[i] != "None":
                    node.right = TreeNode(int(values[i]))
                    next_stack.append(node.right)
                i += 1
            stack = next_stack
        return root


if __name__ == '__main__':
    from utils.maketree import maketree

    my_tree = maketree([1, 2, 4, 5, 8, 9, 3, 6, 7], [4, 2, 8, 5, 9, 1, 6, 3, 7])
    #        1
    #     /      \
    #     2       3
    # /

    s = Codec()
    # answer = s.serialize(my_tree)
    ans = [1, 2, 3, None, None, 4, 5]
    answer = ",".join([str(item) for item in ans])
    print(s.deserialize(answer))
