#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/8 12:33
# @Author  : frelikeff
# @Site    : 
# @File    : 199answer.py
# @Software: PyCharm
from utils.maketree import TreeNode, maketree
from typing import List


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans = []
        deque = [root]
        while deque:
            ans.append(deque[-1].val)
            next_deque = []
            for node in deque:
                if node.left:
                    next_deque.append(node.left)
                if node.right:
                    next_deque.append(node.right)
            deque = next_deque
        return ans


if __name__ == '__main__':
    my_tree = maketree([1, 2, 5, 3, 4], [2, 5, 1, 3, 4])
    ans = Solution().rightSideView(my_tree)
    print(ans)
