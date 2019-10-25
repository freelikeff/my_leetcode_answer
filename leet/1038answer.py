#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/1 8:33
# @Author  : frelikeff
# @Site    : 
# @File    : 1038answer.py
# @Software: PyCharm
from utils.maketree import TreeNode, maketree, BT_level_order_traversal


def DLRnodg(root: TreeNode):
    ans = []
    stack = []
    if not root:
        return []

    stack.append(root)
    while stack:
        cur_node = stack.pop()
        if cur_node:
            ans.append(cur_node.val)
            stack.extend([cur_node.right, cur_node.left])
    return ans


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        pre = sorted(DLRnodg(root), reverse=True)
        func = {pre[0]: pre[0]}
        for i in range(1, len(pre)):
            temp = pre[i]
            pre[i] += pre[i - 1]
            func[temp] = pre[i]

        stack = []
        stack.append(root)
        while stack:
            cur_node = stack.pop()
            if cur_node:
                cur_node.val = func[cur_node.val]
                stack.extend([cur_node.right, cur_node.left])
        return root

# 这个是真的屌 # TODO
class Solution2:
    def bstToGst(self, root: TreeNode) -> TreeNode:

        def postOrder(nd, acc=0) -> int:
            if not nd: return acc
            nd.val += postOrder(nd.right, acc)
            return postOrder(nd.left, nd.val)

        postOrder(root)
        return root


if __name__ == '__main__':
    s = Solution()
    my_tree = maketree([4, 1, 0, 2, 3, 6, 5, 7, 8], list(range(9)))
    print(BT_level_order_traversal(my_tree))
    ans = s.bstToGst(my_tree)

    print(BT_level_order_traversal(ans))
