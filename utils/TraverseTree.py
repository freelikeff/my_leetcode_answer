#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/20 20:54
# @Author  : frelikeff
# @Site    : 
# @File    : TraverseTree.py
# @Software: PyCharm
"""
LR代表左右，D代表根
part1
整理了一下前中后的递归非递归遍历,一共三个类，分别表示三种遍历，每个类有两个方法，递归与非递归
part2
morris三种遍历，一个类，三种方法，空间复杂度O（1）
"""
from utils.maketree import TreeNode, maketree


# 前序遍历 Preorder Traversal
class PreorderTraversal:
    # 递归的就没什么好描述了
    def DLR_dg(self, root: TreeNode):
        if not root:
            return []
        return [root.val] + self.DLR_dg(root.left) + self.DLR_dg(root.right)

    # 简单来说就是自构栈，每次访问一个节点后，就把右节点和左节点入栈，如果有的话
    # 那么这样顺序就是根，左（因为是栈），右
    def DLR_ndg(self, root: TreeNode):
        if not root:
            return []
        stack = [root]
        ans = []
        while stack:
            temp = stack.pop()
            ans.append(temp.val)
            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)

        return ans


# 中序遍历
class MidorderTraversal:
    # 递归的就没什么好描述了
    def LdR_dg(self, root: TreeNode):
        if not root:
            return []
        return self.LdR_dg(root.left) + [root.val] + self.LdR_dg(root.right)

    def LDR_ndg(self, root: TreeNode):
        if not root:
            return []
        stack = [(root, False)]
        ans = []
        while stack:
            node, flag = stack.pop()
            if flag:
                ans += [node.val]
            else:
                if node.right:
                    stack.append((node.right, False))
                stack.append((node, True))
                if node.left:
                    stack.append((node.left, False))
        return ans


# 后序遍历
class PostorderTraversal:
    def LRD_dg(self, root: TreeNode):
        if not root:
            return []
        return self.LRD_dg(root.left) + self.LRD_dg(root.right) + [root.val]

    def LRD_ndg(self, root: TreeNode):
        if not root:
            return []
        stack = [(root, False)]
        ans = []
        while stack:
            node, flag = stack.pop()
            if flag:
                ans += [node.val]
            else:
                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))

                if node.left:
                    stack.append((node.left, False))
        return ans

    def LRD_use_DLR(self, root):
        if not root:
            return []
        stack = [root]
        ans = []
        while stack:
            temp = stack.pop()
            ans.append(temp.val)
            if temp.left:
                stack.append(temp.left)
            if temp.right:
                stack.append(temp.right)

        return ans[::-1]


# Morrris Traversal
class MorrisTraversal:
    def LDR(self, root: TreeNode):
        """
        :param root:
        :return: traversal list
        """
        if not root:
            return None

        def findpre(source):  # func功能是寻找前驱节点，所以传进来节点的左节点即可
            node = source.left
            while node.right and node.right != source:
                node = node.right
            return node

        cur = root
        ans = []
        while cur:

            if not cur.left:
                ans.append(cur.val)
                cur = cur.right
                continue

            prenode = findpre(cur)
            if prenode.right == cur:
                ans.append(cur.val)
                cur = cur.right
                prenode.right = None

            else:
                prenode.right = cur
                cur = cur.left

        return ans

    def DLR(self, root: TreeNode):
        if not root:
            return []

        def processnode(source):  # 对于前序遍历，要做的是将node.left的最右节点的left指向node.right,传进来的节点要确保有左节点
            node = source.left
            while node.right or node.left:
                if node.right:
                    node = node.right
                else:
                    node = node.left
            return node

        cur = root
        ans = []
        while cur:
            ans.append(cur.val)
            if not cur.left:
                cur = cur.right

            elif cur.left == cur.right:
                nextnode = cur.left
                cur.left = cur.right = None
                cur = nextnode

            else:
                keynode = processnode(cur)
                keynode.left = keynode.right = cur.right
                cur = cur.left

        return ans

    # TODO,太特么难了
    def LRD(self, root: TreeNode):
        if not root:
            return root


if __name__ == '__main__':
    tree = maketree([4, 2, 1, 3, 6, 5, 7], [1, 2, 3, 4, 5, 6, 7])  # [1, 3, 2, 5, 7, 6, 4]

    s = PostorderTraversal()
    print(s.LRD_dg(tree))
