#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/5 16:10
# @Author  : frelikeff
# @Site    : 
# @File    : 25.py
# @Software: PyCharm
from typing import List
from utils.maketree import TreeNode, maketree


# 这个感觉挺有价值的
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root: TreeNode, target) -> List[List]:
        # 首先是边界条件，这个对于树的题来说都是比较重要的
        if not root:
            return []
        # 然后是简单情况，可以作为递归终止条件
        # 如果左右为空即为叶子节点且值为目标值，那么直接返回答案
        if not root.right and not root.left and root.val == target:
            return [[root.val]]

        ans = []
        # 如果存在左子树
        if root.left:
            # 对于左子树返回的每个元素（是一个列表），加上这个节点值，则可以构成完整路径
            for item in self.FindPath(root.left, target - root.val):
                # 叶子节点给返回结果才加，不然不加入ans
                if len(item):
                    ans.append([root.val] + item)
        # 同上
        if root.right:
            for item in self.FindPath(root.right, target - root.val):
                if len(item):
                    ans.append([root.val] + item)
        return ans


if __name__ == '__main__':
    my_tree = maketree([10, 5, 4, 7, 12], [4, 5, 7, 10, 12])
    target = 22
    s = Solution()

    answer = s.FindPath(my_tree, target)
    print(answer)
