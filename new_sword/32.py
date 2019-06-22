#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/12 18:21
# @Author  : frelikeff
# @Site    : 前两个参考102answer
# @File    : 32.py
# @Software: PyCharm

from utils.maketree import TreeNode, maketree
from typing import List


# 这个层级遍历放回的列表的列表，并且ans不包含null
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        # 初始化ans列表，以及最开始要看的层
        ans = []
        level = [root]
        flag = True
        while level:  # 如果这层还有节点

            cur = []  # 这层的节点值列表，最终添加至ans
            next_level = []  # 这层节点的 左右子节点，也就是下一层
            for node in level:  # 对这层的所有节点进行遍历
                cur.append(node.val)  # 添加值

                # 如果左右存在，那么添加至下一层
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            # 把这层遍历的值结果添加至ans
            # 遍历层置为下一层
            if flag:
                ans.append(cur)
            else:
                ans.append(cur[::-1])

            flag = not flag
            level = next_level
        return ans


if __name__ == '__main__':
    my_tree = maketree([1, 2, 4, 5, 8, 9, 3, 6, 7], [4, 2, 8, 5, 9, 1, 6, 3, 7])
    s = Solution()
    answer = s.levelOrder(my_tree)
    print(answer)
