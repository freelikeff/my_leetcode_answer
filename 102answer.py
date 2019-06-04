#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/4 17:44
# @Author  : frelikeff
# @Site    : 
# @File    : 102answer.py
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

        while level:  # 如果这层还有节点

            cur = []   # 这层的节点值列表，最终添加至ans
            next_level = []   # 这层节点的 左右子节点，也就是下一层
            for node in level:  # 对这层的所有节点进行遍历
                cur.append(node.val)   # 添加值

                # 如果左右存在，那么添加至下一层
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            # 把这层遍历的值结果添加至ans
            # 遍历层置为下一层
            ans.append(cur)
            level = next_level
        return ans


if __name__ == '__main__':
    my_tree = maketree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    s = Solution()
    answer = s.levelOrder(my_tree)
    print(answer)
