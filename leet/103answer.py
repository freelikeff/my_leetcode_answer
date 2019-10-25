#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/5 16:11
# @Author  : frelikeff
# @Site    : 
# @File    : 103answer.py
# @Software: PyCharm
from utils.maketree import TreeNode, maketree
from typing import List


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans=[]
        temp_level=[root]
        flag=True
        while temp_level:
            next_level=[]
            level_values=[]
            for node in temp_level:
                level_values.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if flag:
                ans.append(level_values)
            else:
                ans.append(level_values[::-1])

            temp_level=next_level
            flag= not flag

        return ans




if __name__ == '__main__':
    s = Solution()
    my_tree = maketree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    print(s.zigzagLevelOrder(my_tree))
