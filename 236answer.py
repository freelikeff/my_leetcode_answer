#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/19 21:35
# @Author  : frelikeff
# @Site    : 
# @File    : 236answer.py
# @Software: PyCharm
from utils.maketree import TreeNode, maketree_complex as maketree


# 这个函数是实现祖宗节点到子孙节点的路径，例如[1,0,1],代表root.right.left.right,如果第二个节点不是第一个的子孙节点，返回[]
# 所以这个函数传入的第二个节点不能和第一个节点一样（不仅无意义，而且会产生bug）
def find_children_node(root: TreeNode, child: TreeNode):
    assert root is not child
    if not child or not root:
        return []
    if root.left is child:
        return [0]
    elif root.right is child:
        return [1]
    else:
        part = find_children_node(root.left, child)
        if part:
            return [0] + part
        part = find_children_node(root.right, child)
        if part:
            return [1] + part
        return []


# 空间复杂度还可以，时间效率很差
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 如果两个后代节点有一个是根节点，那么直接返回根节点
        if p is root or q is root:
            return root
        # 记录两个后代节点的路径，那公共祖先则是相同前缀部分
        path1 = find_children_node(root, p)
        path2 = find_children_node(root, q)
        length = min(len(path1), len(path2))
        # 开始从高祖往下传递
        temp = root
        i = 0
        # 传到一个路径结束或者祖先不在相同则返回
        while i < length and path1[i] == path2[i]:
            if path1[i]:
                temp = temp.right
            else:
                temp = temp.left
            i += 1
        return temp


class Solution2:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or p is root or q is root:
            return root

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if not l:
            return r
        if not r:
            return l
        return root


if __name__ == '__main__':
    preorder_seq = [4, 2, 1, 3, 6, 5, 7]
    middleorder_seq = [1, 2, 3, 4, 5, 6, 7]

    my_tree = maketree([1, 2, 4, 5, 8, 9, 3, 6, 7], [4, 2, 8, 5, 9, 1, 6, 3, 7])
    print(hash(TreeNode(7)))
    path = find_children_node(my_tree, TreeNode(7))
    print(path)
    s = Solution()
    ans = s.lowestCommonAncestor(my_tree, my_tree.left.right.left, my_tree.right.right)
    print(ans.val)
