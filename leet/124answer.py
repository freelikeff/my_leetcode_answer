#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/28 16:24
# @Author  : frelikeff
# @Site    : 
# @File    : 124answer.py
# @Software: PyCharm
from utils.maketree import TreeNode, maketree


def helper(root: TreeNode):  # 需要返回两个值，一个是ans,一个是根节点到叶节点的最大值
    if not root.left and not root.right:
        return root.val, root.val
    elif not root.right:
        left_ans, left_top = helper(root.left)
        end = max(left_top + root.val, root.val)
        return max(left_ans, end), end
    elif not root.left:

        right_ans, right_top = helper(root.right)
        end = max(right_top + root.val, root.val)
        return max(right_ans, end), end
    else:
        left_ans, left_top = helper(root.left)
        right_ans, right_top = helper(root.right)
        end = max(left_top + root.val, root.val + right_top, root.val)
        return max(left_ans, right_ans, left_top + root.val + right_top, end), end


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        return helper(root)[0]


if __name__ == '__main__':
    s = Solution()
    mytree = maketree([1, 2, 3], [2, 1, 3])
    print(s.maxPathSum(mytree))
